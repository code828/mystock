
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins,viewsets,filters
from .models import Stock, Stockaddress
from .serializers import StocksSerializer, StocksaddressSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class StockPagination(PageNumberPagination):
    """
        库存列表自定义分页
        """
    # 默认每页显示的个数
    page_size = 10
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
    queryset = Stock.objects.all().order_by('detail','address')
    serializer_class = StocksSerializer
    pagination_class = StockPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)

    filter_fields = ('detail',)
    search_fields = ("name",)

class StockaddressViewset(mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset = Stockaddress.objects.all()
    serializer_class = StocksaddressSerializer
    