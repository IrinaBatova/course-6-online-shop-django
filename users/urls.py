from django.urls import path
from .views import UserRegisterView, UserLoginView, UserlogoutView

app_name = 'users' # Это имя пространства имен для шаблонов

# Маршрутизация (URL-адреса) на уровне приложения "catalog".
# Связывает конкретные пути с контроллерами (функциями-представлениями) в views.
urlpatterns = [
    # Статический маршрут для страницы регистрации по адресу users/register/
    path('register/', UserRegisterView.as_view(), name='register'),
    # Статический маршрут для страницы входа по адресу users/login/
    path('login/', UserLoginView.as_view(), name='login'),
    # Статический маршрут для страницы выхода по адресу users/logout/
    path('logout/', UserlogoutView.as_view(), name='logout'),
]
