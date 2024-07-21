from django.db import models

from cities.models import City

class Street(models.Model):
    name = models.CharField('Название', max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'city')
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    def __str__(self) -> str:
        return self.name
