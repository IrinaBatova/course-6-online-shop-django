from django.urls import path
# from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail, create_product

# appname = CatalogConfig.name
app_name = 'catalog'

# Маршрутизация (URL-адреса) на уровне приложения "catalog".
# Связывает конкретные пути с контроллерами (функциями-представлениями) в views.py
urlpatterns = [
    # Статический маршрут (Главная страница каталог)
    path('', home, name='home'),
    # Статический маршрут (страница контакты)
    path('contacts/', contacts, name='contacts'),
    # Динамический маршрут (страница с подробной информацией о товаре)
    path('product/<int:pk>/', product_detail, name='product_detail'),
    # Статический маршрут (страница для добавления новых товаров)
    path('product/create/', create_product, name='create_product'),
]
