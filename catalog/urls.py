from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

appname = CatalogConfig.name

# Маршрутизация (URL-адреса) на уровне приложения "catalog".
# Связывает конкретные пути с функциями-представлениями (views).
urlpatterns = [
    # Статический маршрут (Главная страница каталог)
    path('', home, name='home'),
    # Статический маршрут (страница контакты)
    path('contacts/', contacts, name='contacts'),
]
