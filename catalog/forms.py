from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #Поля можно указать одним из способов:
        # 1 - указать поля для вывода;
        # 2- указать все доступные поля;
        # 3 - указать поля, которые не нужно выводить
        fields = 'category', 'name', 'description', 'image', 'price', 'manufactured_at'
        #exclude = 'created_at', 'updated_at'
        #fields = '__all__'


