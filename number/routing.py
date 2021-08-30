from django.urls import path
from number.consumers import PrizeConsumer


websocket_urlpatterns = [
    path('ws/prize/', PrizeConsumer.as_asgi()),
]
