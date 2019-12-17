from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins,viewsets,filters
from .models import Stock, Stockaddress,Stockrecrod
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


class StockViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    """
    库存列表
    """
    queryset = Stock.objects.all().order_by('address','detail')
    serializer_class = StocksSerializer
    pagination_class = StockPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)

    filter_fields = ('address',)
    search_fields = ("name",)

    def perform_update(self, serializer):
        record = serializer.save()
        record_stock = Stockrecrod()
        record_address = Stockaddress()
        #更新stock:
        #stock = Stock()
        #stock.address = record.address
        #stock.save()
        # 获取修改之前的地址
        existed_record = Stock.objects.get(id=serializer.instance.id)
        record_stock.stocks_id = serializer.instance.id
        record_stock.oldaddress = Stockaddress.objects.get(address=existed_record.address)
        record_stock.olddetail = serializer.instance.detail
        record_stock.add_time = datetime.now()
        record_stock.ways = '1'
        record_stock.save()

class StockaddressViewset(mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset = Stockaddress.objects.all()
    serializer_class = StocksaddressSerializer
    