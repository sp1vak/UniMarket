from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UniUser(AbstractUser):
    description = models.CharField(max_length=125, verbose_name='Description', default="-", blank=True)
    balance = models.IntegerField(verbose_name="Balance", default=0)
    avatar = models.ImageField(verbose_name="Avatar", blank=True)
    is_online = models.BooleanField(default=False)

class Category(models.Model):
    name=models.CharField(verbose_name="Name")
    def __str__(self):
        return self.name
    
class Product(models.Model):
   name = models.CharField(verbose_name="Name")
   price = models.IntegerField(verbose_name='Price', default=10, null=True)
   image = models.ImageField(verbose_name="Image", default='avatar.jpeg')
   description = models.CharField(max_length=125, verbose_name="Pr_Description", default='-')
   category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
   seller = models.ForeignKey(UniUser, on_delete=models.CASCADE, verbose_name="Seller")

class Basket(models.Model):
    user = models.ForeignKey(UniUser, on_delete=models.CASCADE, verbose_name="User")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveBigIntegerField(verbose_name="Quantity")
    time_added = models.DateTimeField(verbose_name="Date",auto_now_add=True)