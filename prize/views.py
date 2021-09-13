from rest_framework.generics import ListAPIView
from prize.serializers import PrizeSerializer
from number.models import Number
from rest_framework.permissions import IsAuthenticated


class PrizeListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PrizeSerializer

    def get_queryset(self):
        return Number.objects.filter(user_id=self.request.user, won=True)
