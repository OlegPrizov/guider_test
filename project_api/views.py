from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from cities.models import City
from shops.models import Shop
from streets.models import Street

from .serializers import CitySerializer, ShopCreateSerializer, ShopListSerializer, StreetSerializer

from .filters import ShopFilter

class CityViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class ShopCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopCreateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ShopCreateSerializer
        return ShopListSerializer

class StreetViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        if city_id:
            return Street.objects.filter(city_id=city_id)
        return Street.objects.all()
