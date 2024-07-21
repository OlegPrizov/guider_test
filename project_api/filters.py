import pytz

import django_filters
from django.utils import timezone

from shops.models import Shop


class ShopFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='city__name', lookup_expr='icontains')
    street = django_filters.CharFilter(field_name='street__name', lookup_expr='icontains')
    open = django_filters.NumberFilter(method='filter_open')

    def filter_open(self, queryset, name, value):
        moscow_tz = pytz.timezone('Europe/Moscow')
        now = timezone.now().astimezone(moscow_tz).time()
        print(now)
        if value == 1:  # открыто
            # Магазин открыт, если текущее время находится между временем открытия и временем закрытия
            return queryset.filter(
                opening_time__lte=now,
                closing_time__gte=now
            )
        elif value == 0:  # закрыто
            #  Магазин заткрыт, если время открытия больше чем сейчас или время закрытия меньше чем сейчас
            return queryset.filter(
                opening_time__gt=now
            ) | queryset.filter(
                closing_time__lt=now
            )
        return queryset

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']