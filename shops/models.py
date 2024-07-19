from django.db import models

from cities.models import City
from streets.models import Street

class Shop(models.Model):
    name = models.CharField('Название', max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_number = models.IntegerField('Номер дома')
    opening_time = models.TimeField('Время открытия')
    closing_time = models.TimeField('Время закрытия')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self) -> str:
        return self.title
