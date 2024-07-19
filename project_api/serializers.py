from rest_framework import serializers

from cities.models import City
from streets.models import Street
from shops.models import Shop

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    srteet = StreetSerializer()

    class Meta:
        model = Shop
        fields = '__all__'