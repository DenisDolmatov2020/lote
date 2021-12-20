from rest_framework import serializers
from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = '__all__'
