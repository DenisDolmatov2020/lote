from rest_framework import serializers
from lot.models import Lot, Image, Condition
from my_user.models import User
from my_user.serializers import UserSerializer
from number.serializers import NumberSerializer


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'
        read_only_fields = ('lot',)


class LotImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url']
        read_only_fields = ('lot',)


class LotSerializer(serializers.ModelSerializer):
    images = LotImageSerializer(many=True, required=False)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        source='user',
        write_only=True
    )
    conditions = ConditionSerializer(many=True, required=False)
    wins = NumberSerializer(many=True, read_only=True)
    free_numbers = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Lot
        fields = '__all__'

    def create(self, validated_data):
        conditions_data = validated_data.pop('conditions', [])
        lot = Lot.objects.create(**validated_data)
        if conditions_data:
            Condition.objects.bulk_create(
                Condition(lot=lot, **condition)
                for condition in conditions_data
            )
        return lot


class LotPrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ['id', 'title']
