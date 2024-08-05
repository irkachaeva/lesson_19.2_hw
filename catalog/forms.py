from django import forms
from catalog.models import Product

stop_text = "казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар"
stop_words = set(stop_text.split(", "))


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        words = set(cleaned_data.lower().split())
        if words.intersection(stop_words):
            raise forms.ValidationError('Ошибка, связанная с названием продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        words = set(cleaned_data.lower().split())
        if words.intersection(stop_words):
            raise forms.ValidationError('Ошибка, связанная с описанием продукта')
        return cleaned_data