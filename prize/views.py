from typing import Union

from rest_framework.generics import ListAPIView
from prize.serializers import PrizeSerializer
from number.models import Number
from rest_framework.permissions import IsAuthenticated


class PrizeListView(ListAPIView):
    permission_classes = IsAuthenticated
    serializer_class = PrizeSerializer

    def get_queryset(self):
        user = self.request.user
        prizes = Number.objects.filter(user_id=user, won=True)
        return prizes
