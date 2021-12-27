from rest_framework import serializers
from shop.models import Shop, ShopCondition, ShopComment


class ShopConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCondition
        fields = '__all__'


class ShopCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopComment
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    conditions = ShopConditionSerializer(many=True, required=False)
    comments = ShopCommentSerializer(many=True, required=False)
    group = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = '__all__'
