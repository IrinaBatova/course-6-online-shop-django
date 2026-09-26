from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# Маршрутизация.
# Главный диспетчер URL-адресов на уровне проекта. Подключает URL-адреса страниц приложений в общую структуру проекта.
# Django берет все маршруты, которые написаны внутри файла например blog/urls.py, и прибавляет к началу каждого из них
# префикс blog/. Исключение, если стоит '', это главное приложение проекта (сайта) и к страницам этого приложения
# префикс не прибавляется, эти страницы открываются сразу по корневому адресу сайта.
urlpatterns = [
    # Маршруты для встроенной панели администратора Django
    path('admin/', admin.site.urls), # admin.site.urls это встроенный в Django набор маршрутов
    # Маршруты для главного приложения проекта (сайта) 'catalog', подключаются URL-адреса страниц приложения catalog
    path('', include('catalog.urls', namespace='catalog')),
    # Маршруты для приложения 'blog', подключаются URL-адреса страниц приложения blog
    path('blog/', include('blog.urls', namespace='blog')),
]

# Добавляем раздачу медиафайлов в режиме отладки (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
