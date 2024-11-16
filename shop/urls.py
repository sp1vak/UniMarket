from django.urls import path
from .views import shop, product

urlpatterns = [
    path('', shop, name='shop'),
    path('product/<int:product_id>/', product, name='product'),
]