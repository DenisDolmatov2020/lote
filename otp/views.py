import os
from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from lottee_new.helpers import get_object_or_none
from otp.models import OTP
from otp.serializers import OTPSerializer
from otp.tasks import send_code


class OTPCreateView(CreateAPIView):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

    def create(self, request, *args, **kwargs):
        otp = get_object_or_none(OTP, identifier=request.data['identifier'])
        if otp:
            if timezone.now() - timedelta(seconds=int(os.environ.get('TIMER_TIME'))) > otp.created:
                otp.delete()
            else:
                return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            otp = serializer.save()
            send_code(otp.identifier, otp.code)
            return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def verify(request, *args, **kwargs):
    otp = get_object_or_none(OTP, identifier=request.data['identifier'], code=request.data['code'])
    if otp:
        otp.verified = True
        otp.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)
