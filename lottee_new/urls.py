from django.contrib import admin
from django.urls import path, include
from number.views import NumberUpdateView
from prize.views import PrizeListView
from tracker.views import TrackerView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/my-user/', include('my_user.urls')),
    path('api/otp/', include('otp.urls')),
    path('api/lot/', include('lot.urls')),
    path('api/number/', NumberUpdateView.as_view(), name='NumberUpdateView'),
    path('api/prize/', PrizeListView.as_view(), name='PrizeListView'),
    path('api/tracker', TrackerView.as_view(), name='tracker-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
