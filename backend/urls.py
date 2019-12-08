from django.urls import path,include

from backend.views import StockaddressViewset
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'stocks',views.StockViewset)
router.register(r'address',StockaddressViewset)

urlpatterns = [
    path('',include(router.urls))
]