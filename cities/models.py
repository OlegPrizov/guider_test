from django.db import models

class City(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self) -> str:
        return self.title
