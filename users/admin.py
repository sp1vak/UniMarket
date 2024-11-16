from django.contrib import admin
from .models import UniUser, Category, Product, Basket

# Register your models here.
@admin.register(UniUser)
class UniUserAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    ...