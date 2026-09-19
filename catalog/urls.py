from django.urls import path
# from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView

# appname = CatalogConfig.name
app_name = 'catalog'

# Маршрутизация (URL-адреса) на уровне приложения "catalog".
# Связывает конкретные пути с контроллерами (функциями-представлениями) в views.py
urlpatterns = [
    # Статический маршрут (Главная страница каталог)
    # path('', home, name='home'),
    path('', ProductListView.as_view(), name='home'),
    # Статический маршрут (страница контакты)
    path('contacts/', ContactsView.as_view(), name='contacts'),
    # Динамический маршрут (страница с подробной информацией о товаре)
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # Статический маршрут (страница для добавления новых товаров)
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
]
