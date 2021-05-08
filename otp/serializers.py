import random
from rest_framework import serializers, validators
from otp.models import OTP


class OTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = OTP
        fields = ['identifier']

    '''def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(OTPSerializer, self).run_validators(value)'''

    def create(self, validated_data):
        validated_data['code'] = random.randrange(100000, 999999)
        instance = OTP.objects.create(**validated_data)
        return instance
