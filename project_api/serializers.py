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

class ShopCreateSerializer(serializers.ModelSerializer):
    city = serializers.CharField()
    street = serializers.CharField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house_number', 'opening_time', 'closing_time']

    def create(self, validated_data):
        city_name = validated_data.pop('city')
        street_name = validated_data.pop('street')
        city, _ = City.objects.get_or_create(name=city_name)
        street, _ = Street.objects.get_or_create(name=street_name, city=city)
        return Shop.objects.create(city=city, street=street, **validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {'id': representation['id']}

class ShopListSerializer(serializers.ModelSerializer):
    city = serializers.CharField()
    street = serializers.CharField()

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city', 'street', 'house_number', 'opening_time', 'closing_time']