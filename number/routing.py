from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/prize/', consumers.PrizeConsumer.as_asgi()),
]
