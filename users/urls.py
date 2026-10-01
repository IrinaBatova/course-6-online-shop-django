from django.urls import path
from .views import UserRegisterView, UserLoginView, UserlogoutView

app_name = 'users' # Это имя пространства имен для шаблонов

# Маршрутизация (URL-адреса) на уровне приложения "catalog".
# Связывает конкретные пути с контроллерами (функциями-представлениями) в views.
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserlogoutView.as_view(), name='logout'),
]
