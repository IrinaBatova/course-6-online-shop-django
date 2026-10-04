from django.urls import path
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = 'catalog' # Это имя пространства имен для шаблонов

# Маршрутизация (URL-адреса) на уровне приложения "catalog".
# Связывает конкретные пути с контроллерами (функциями-представлениями) в views.py
urlpatterns = [
    # Статический маршрут (Главная страница каталог), открывается сразу по корневому адресу сайта
    path('', ProductListView.as_view(), name='home'),
    # Статический маршрут (страница контакты)
    path('contacts/', ContactsView.as_view(), name='contacts'),
    # Динамический маршрут (страница с подробной информацией о товаре)
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # Статический маршрут (страница для добавления нового товара)
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    # Динамический маршрут (страница для изменения товара)
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
