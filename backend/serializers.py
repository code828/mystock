from rest_framework import serializers
from .models import Stock, Stockaddress


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("id","code","name","bar_tmp","barcode","place","detail","address")

class StocksaddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stockaddress
        fields = ("__all__")