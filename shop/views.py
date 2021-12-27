# from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from shop.models import Shop, ShopCondition, ShopComment
from shop.serializers import ShopSerializer


@api_view(['GET'])
def shop_detail_view(request, slug):
    print(slug)
    shop = get_object_or_404(Shop, slug=slug)
    shop.conditions = ShopCondition.objects.filter(active=True, shop_id=shop.id)
    shop.comments = ShopComment.objects.filter(active=True, shop_id=shop.id)
    serializer = ShopSerializer(shop)
    print(serializer.data)
    return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class ShopListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
