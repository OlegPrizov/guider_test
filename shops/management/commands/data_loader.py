from datetime import time

from django.core.management.base import BaseCommand

from shops.models import Shop
from streets.models import Street
from cities.models import City

city_name = 'Москва'
streets = ['Мясницкая', 'Никольская']
shops = [
    [['БукВышка', 20, 10, 19], ['Библио-Глобус', 6, 10, 21], ['Surf Coffee', 8, 1, 11]], 
    [['Мангазея', 17, 12, 20], ['Оптик-А', 8, 10, 22], ['Азбука вкуса', 7, 1, 10]]
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        city, created = City.objects.get_or_create(name=city_name)
        for street in streets:
            Street.objects.get_or_create(
                city = city,
                name = street
            )
        myasnitskaya, created = Street.objects.get_or_create(name = streets[0])
        nikolskaya, created = Street.objects.get_or_create(name = streets[1])
        for index, row in enumerate(shops):
            for shop in row:
                opening_time = time(shop[2], 0)
                closing_time = time(shop[3], 0)
                Shop.objects.get_or_create(
                    name=shop[0],
                    city=city,
                    street=myasnitskaya if index == 0 else nikolskaya,
                    house_number=shop[1],
                    opening_time=opening_time,
                    closing_time=closing_time
                )
        print('Загрузка закончилась')