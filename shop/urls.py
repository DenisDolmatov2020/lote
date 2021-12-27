from django.urls import path
from shop.views import ShopListView, shop_detail_view


urlpatterns = [
    path('<slug:slug>/', shop_detail_view, name='detail-shop'),
    path('', ShopListView.as_view(), name='list-shops')
]
