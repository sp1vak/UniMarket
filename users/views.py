from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Basket, Product
from .forms import UniUserCreationForm, UniUserEditionForm, CreateProduct

# Create your views here.
class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context = {
            'form': UniUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UniUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

@login_required
def profile(request):
    basket = Basket.objects.filter(user=request.user)[:2]
    return render(request, "profile.html", {'basket': basket})
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UniUserEditionForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/profile/')
    else:
        form = UniUserEditionForm(instance = request.user)
    return render(request, 'editprofile.html', {'form': form})

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket= baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect('/shop/')

@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect('/users/profile/')

@login_required
def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    return render(request, 'basket.html', {"baskets": baskets})

@login_required
def add_product(request):
    form = CreateProduct()
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.seller = request.user
            post.save()
            return HttpResponseRedirect('/users/profile/')
    else:
        form = CreateProduct()
    return render(request, 'add_product.html', {'form': form})