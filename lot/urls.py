from rest_framework.routers import DefaultRouter
from lot.views import LotViewSet


router = DefaultRouter()
router.register(r'', LotViewSet, basename='lots')
urlpatterns = router.urls
