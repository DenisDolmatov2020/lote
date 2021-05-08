from my_user.views import \
    UserCreateView, UserRetrieveUpdateView, UpdatePasswordView, have_account, free_account, reset_password
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # user
    path('have-account/', have_account),
    path('free-account/', free_account),
    path('create/', UserCreateView.as_view(), name='create'),
    path('', UserRetrieveUpdateView.as_view(), name='retrieve-update'),
    # token
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    # password
    path('update-password/', UpdatePasswordView.as_view(), name='update-password'),
    path('reset-password/', reset_password),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
