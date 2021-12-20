from django.urls import path
from shop.views import ShopDetailView, ShopListView


urlpatterns = [
    path('<slug:slug>', ShopDetailView.as_view(), name='detail-shop'),
    path('', ShopListView.as_view(), name='list-shops')
]
