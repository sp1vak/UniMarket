from django.shortcuts import render
from users.models import Product

# Create your views here.
def shop(request):
    product = Product.objects.all()
    return render(request, "shop.html", {'product': product})

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})