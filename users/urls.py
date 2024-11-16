from django.urls import path, include
from .views import Register, profile, edit_profile, basket_add, basket_delete, basket, add_product

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name = 'register'),
    path('profile/', profile, name = 'profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:basket_id>/', basket_delete, name='basket_delete'),
    path('basket/', basket, name='basket'),
    path('add_products/', add_product, name='add_product'),
]