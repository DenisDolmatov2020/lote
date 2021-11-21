from django.contrib import admin
from django.urls import path, include
from prize.views import PrizeListView
from rules.views import RulesListView
from tracker.views import TrackerView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/my-user/', include('my_user.urls')),
    path('api/otp/', include('otp.urls')),
    path('api/lot/', include('lot.urls')),
    path('api/number/', include('number.urls')),
    path('api/prize/', PrizeListView.as_view(), name='prize-list'),
    path('api/tracker', TrackerView.as_view(), name='tracker-view'),
    path('api/rules', RulesListView.as_view(), name='rules-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
