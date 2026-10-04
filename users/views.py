from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class UserRegisterView(CreateView):
    """Контроллер для регистрации пользователя"""
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'  # Путь к шаблону регистрации
    success_url = reverse_lazy('users:login')  # Перенаправление после успешной регистрации

    def form_valid(self, form):
        # Сохраняем пользователя в базу данных
        user = form.save()

        # Логика отправки приветственного письма
        send_mail(
            subject='Добро пожаловать!',
            message=f'Здравствуйте! Вы успешно зарегистрировались на сайте интернет-магазина Skystore. Ваш логин для входа: {user.email}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return super().form_valid(form)


class UserLoginView(LoginView):
    """Контроллер для авторизации пользователя"""
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'  # Путь к шаблону авторизации


class UserlogoutView(LogoutView):
    """Контроллер для выхода пользователя"""
    next_page = reverse_lazy('catalog:home')  # Куда перенаправлять после выхода

