from django.db import models
from datetime import datetime

# Create your models here.
class Stockaddress(models.Model):
    address = models.CharField(max_length=30)

class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    goal = models.CharField(max_length=10)
    bar_tmp = models.CharField(max_length=21)
    barcode = models.CharField(max_length=21)
    kind = models.CharField(max_length=8)
    purchase_date = models.DateTimeField()
    purchase_method = models.CharField(max_length=6)
    attribute = models.CharField(max_length=8)
    serial = models.CharField(max_length=10)
    price = models.IntegerField()
    user = models.CharField(max_length=30)
    number = models.CharField(max_length=5)
    keeper = models.CharField(max_length=4)
    code_place = models.CharField(max_length=8)
    place = models.CharField(max_length=30)
    status = models.CharField(max_length=4)
    detail = models.CharField(max_length=30)
    out_date = models.DateTimeField()
    address = models.CharField(max_length=30)

class Stockrecrod(models.Model):
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name="库存", related_name="records")
    ways = models.CharField(max_length=1)
    oldaddress = models.ForeignKey(Stockaddress, on_delete=models.CASCADE, verbose_name="库存地", related_name="old")
    newaddress = models.ForeignKey(Stockaddress, on_delete=models.CASCADE, verbose_name="库存地", related_name="new")
    add_time = models.DateTimeField("记录时间", default=datetime.now)