import random
from rest_framework.generics import ListAPIView, UpdateAPIView
from number.models import Number
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from number.serializers import NumberSerializer
from number.service import choose_winners


class NumberList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NumberSerializer

    def get_queryset(self):
        return Number.objects.filter(user=self.request.user)


class NumberUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        numbers = Number.objects.select_related('lot__user').filter(lot_id=self.request.data['lot_id'])
        lot_user_numbers = numbers.filter(user_id=request.user.id)
        lot_numbers_free = numbers.filter(user_id=None)
        if lot_numbers_free:
            random_idx = random.randint(0, len(lot_numbers_free) - 1)
            lot_number = lot_numbers_free[random_idx]
            energy = lot_number.lot.energy * (2 ** len(lot_user_numbers))
            if request.user.energy >= energy and request.user != lot_number.lot.user:
                request.user.energy -= energy
                request.user.save(update_fields=['energy'])
                lot_number.user = request.user
                lot_number.save(update_fields=['user'])
                if len(lot_numbers_free) <= 1 and lot_number.lot.active:
                    choose_winners(lot_number.lot)
                return Response(
                    status=status.HTTP_200_OK,
                    data=lot_number.num
                )
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
