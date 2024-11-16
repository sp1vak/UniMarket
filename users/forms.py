from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from users.models import Product, Category

# Create your forms here.
class UniUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

class UniUserEditionForm(UserChangeForm):
    password = None
    avatar = forms.ImageField(required=False, error_messages={'invalid': "Images files only."}, widget=forms.FileInput)
    class Meta:
        model = get_user_model()
        fields = ("avatar", "username", "email", "description")

class CreateProduct(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)
    price = forms.IntegerField(required=False)
    image = forms.ImageField(error_messages={'invalid': 'Images files only.'}, widget=forms.FileInput, required=False)
    description = forms.Textarea()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'dropdown'}), required=False)
    class Meta:
        model = Product
        fields = ('name', 'price', 'image', 'description', 'category')