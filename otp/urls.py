from django.urls import path

from otp.views import OTPCreateView, verify

urlpatterns = [
    path('verify/', verify),
    path('', OTPCreateView.as_view(), name='create-otp'),
    # path('verify/', UserRetrieveUpdateView.as_view(), name='verify'),
]
