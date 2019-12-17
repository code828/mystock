from django.db import models
from datetime import datetime

# Create your models here.
class Stockaddress(models.Model):
    address = models.CharField(max_length=30)

class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(default="", max_length=30)
    goal = models.CharField(default="", max_length=10)
    bar_tmp = models.CharField(max_length=21)
    barcode = models.CharField(default='',max_length=21)
    kind = models.CharField(default="", max_length=8)
    purchase_date = models.DateTimeField(default=datetime.now)
    purchase_method = models.CharField( max_length=6)
    attribute = models.CharField(default="",max_length=8)
    serial = models.CharField(default="",max_length=10)
    price = models.IntegerField(default=0)
    user = models.CharField(default="",max_length=30)
    number = models.CharField(default="",max_length=5)
    keeper = models.CharField(default="",max_length=4)
    code_place = models.CharField(default="",max_length=8)
    place = models.CharField(default="",max_length=30)
    status = models.CharField(default="",max_length=4)
    detail = models.CharField(default="",max_length=30)
    out_date = models.DateTimeField(default=datetime.now)
    address = models.CharField(default="",max_length=30)
    tag = models.CharField(max_length=18,default='')

class Stockrecrod(models.Model):
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name="库存", related_name="records")
    ways = models.CharField(default="",max_length=1)
    olddetail = models.CharField(default="",max_length=30)
    oldaddress = models.ForeignKey(Stockaddress, on_delete=models.CASCADE, verbose_name="库存地", related_name="old")
    add_time = models.DateTimeField("记录时间", default=datetime.now)