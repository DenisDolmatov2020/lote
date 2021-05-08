from rest_framework import serializers
from number.models import Number
from my_user.serializers import UserSerializer


class NumberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Number
        fields = ['user', 'id', 'lot', 'num']


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['user', 'num']
