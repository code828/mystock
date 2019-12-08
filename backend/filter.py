import django_filters

from .models import Stock

class StockFilter(django_filters.rest_framework.FilterSet):
    search_address = django_filters.CharFilter(name='detail',lookup_expr='exact')

    class Meta:
        model = Stock
        fields = ['detail',]