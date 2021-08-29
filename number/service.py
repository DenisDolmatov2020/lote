import os

import requests
from channels.layers import get_channel_layer
from rest_framework.utils import json
from number.models import Number
from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

from number.serializers import WinnerSerializer


def choose_winners(lot):
    data_ = [1]
    if lot.players > 1:
        url = 'https://api.random.org/json-rpc/2/invoke'
        json_ = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": os.getenv("RANDOM_API_KEY"),
                "n": lot.winners,
                "min": 1,
                "max": lot.players,
                "replacement": False
            },
            "id": lot.id
        }
        r = requests.post(url, json=json_)
        json_ = json.loads(r.text)
        lot.winners_complete = json_['result']['random']['completionTime']
        data_ = json_['result']['random']['data']

    winners = Number.objects.filter(lot=lot, num__in=data_)  # .update(won=True)
    lot.active = False
    lot.save()

    winners_serializer = WinnerSerializer(winners, many=True)
    winners.update(won=True)
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('prize', {
        'type': 'have_prize',
        'lot': {
            'id': lot.id,
            'title': lot.title,
            'winners': winners_serializer.data
        }
    })
