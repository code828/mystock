from django.shortcuts import render
from rest_framework import mixins,viewsets
from .models import Stock
from .serializers import StocksSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class StockPagination(PageNumberPagination):
    """
        库存列表自定义分页
        """
    # 默认每页显示的个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class StockViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    库存列表
    """
    queryset = Stock.objects.all()
    serializer_class = StocksSerializer
    pagination_class = StockPagination
    