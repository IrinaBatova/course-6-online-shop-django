from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    """Форма для регистрации пользователя по email без username"""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')  # Указываем какие поля выводить в форму

    # Метод для стилизации полей
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Переводим заголовки полей на русский язык
        if 'password1' in self.fields:
            self.fields['password1'].label = "Пароль"
        if 'password2' in self.fields:
            self.fields['password2'].label = "Подтверждение пароля"

        # Перебираем все поля формы и добавляем им Bootstrap-класс
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    """Форма для аутентификации по email"""

    # Переопределяем стандартное поле username
    username = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control'})
    )

    # Переопределяем стандартное поле password
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
