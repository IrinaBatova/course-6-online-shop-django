from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для модели Product"""

    # Список запрещенных слов
    FORBIDDEN_WORDS = [
        'казино', 'биржа', 'обман',
        'криптовалюта', 'дешево', 'полиция',
        'крипта', 'бесплатно', 'радар'
    ]

    class Meta:
        """Специальный служебный класс, где указываются глобальные параметры для Django"""

        # Указываем с какой моделью связана эта форма
        model = Product

        # Перечисляем поля модели, которые пользователь будет заполнять на форме
        fields = ('name', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        """Красиво оформляет поля формы с помощью классов Bootstrap 5"""

        # Сначала вызываем родительский метод инициализации Django, чтобы он создал стандартные поля
        super().__init__(*args, **kwargs)

        # Цикл, который перебирает все поля, указанные в fields класса Meta
        for field_name, field in self.fields.items():
            # Проверяем имя конкретного поля, чтобы применить к нему индивидуальный внешний вид
            if field_name == 'image':
                # Динамически добавляем к HTML-тегам полей CSS-классы фреймворка Bootstrap
                field.widget.attrs.update({'class': 'form-control-file'})
            elif field_name == 'category':
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

    # Кастомная очистка (валидация) в методах clean_name и clean_description введенных пользователем данных

    def clean_name(self):
        """Кастомный метод-обработчик, для кастомной проверки (валидации) поля name"""

        # В self.cleaned_data попадают только те поля, которые успешно прошли все базовые (N: соответствие типа
        # данных) проверки методом is_valid(), который Django вызывает у формы автоматически под капотом внутри
        # CBV-контроллеров CreateView или UpdateView.
        cleaned_data = self.cleaned_data.get('name')

        # Приводим к нижнему регистру для проверки в любом регистре
        lower_name = cleaned_data.lower()

        for word in self.FORBIDDEN_WORDS:
            if word in lower_name:
                raise ValidationError(f'В названии нельзя использовать слово "{word}".')

        return cleaned_data

    def clean_description(self):
        """Кастомный метод-обработчик, для кастомной проверки(валидации) поля description"""
        cleaned_data = self.cleaned_data.get('description')
        lower_description = cleaned_data.lower()

        for word in self.FORBIDDEN_WORDS:
            if word in lower_description:
                raise ValidationError(f'В описании нельзя использовать слово "{word}".')

        return cleaned_data

    def clean_price(self):
        """Кастомный метод-обработчик, для кастомной проверки (валидации) поля price"""

        # В self.cleaned_data попадают только те поля, которые успешно прошли все базовые (N: соответствие типа
        # данных) проверки методом is_valid(), который Django вызывает у формы автоматически под капотом внутри
        # CBV-контроллеров CreateView или UpdateView.
        cleaned_data = self.cleaned_data.get('price')

        if cleaned_data < 0:
            raise ValidationError(f'Цена не может быть отрицательной "{cleaned_data}".')

        return cleaned_data
