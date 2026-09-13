from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Перечисляем поля модели, которые пользователь будет заполнять на форме
        fields = ('name', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        """Красиво оформляет поля формы с помощью классов Bootstrap 5"""
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs.update({'class': 'form-control'})
            elif field_name == 'category':
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
