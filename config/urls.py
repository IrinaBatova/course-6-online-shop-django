from django.contrib import admin
from django.urls import path, include

# Маршрутизация (главный диспетчер URL-адресов) на уровне проекта.
# Связывает URL-адреса с конкретными приложениями или представлениями (views).
urlpatterns = [
    # Маршрут для встроенной панели администратора Django
    path('admin/', admin.site.urls), # admin.site.urls это встроенный в Django набор маршрутов (контроллеров)
    # Включение URL-адресов приложения catalog в общую структуру проекта
    path('', include('catalog.urls')),
]
