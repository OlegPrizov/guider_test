from django.urls import include, path
from rest_framework import routers

from .views import CityViewSet, StreetViewSet, ShopCreateViewSet

app_name = 'project_api'

router = routers.DefaultRouter()
router.register('city', CityViewSet)
router.register('shop', ShopCreateViewSet)
router.register('city/(?P<city_id>\d+)/street', StreetViewSet, basename='city-street')

urlpatterns = [
    path('', include(router.urls)),
]
