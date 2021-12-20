# from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.views.generic.detail import DetailView
from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.viewsets import ViewSet
# from backcashapi.permissions import ReadOnly
from shop.models import Shop
from shop.serializers import ShopSerializer


class ShopDetailView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'slug'


class ShopListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
