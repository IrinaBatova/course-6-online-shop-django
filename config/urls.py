from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from catalog.urls import appname

# Маршрутизация (главный диспетчер URL-адресов) на уровне проекта.
# Связывает URL-адреса с конкретными приложениями или представлениями (views).
urlpatterns = [
    # Маршрут для встроенной панели администратора Django
    path('admin/', admin.site.urls), # admin.site.urls это встроенный в Django набор маршрутов (контроллеров)
    # Включение URL-адресов приложения catalog в общую структуру проекта
    path('', include('catalog.urls', namespace='catalog')),
    # Включение URL-адресов приложения blog в общую структуру проекта
    path('blog/', include('blog.urls', namespace='blog')),
]

# Добавляем раздачу медиафайлов в режиме отладки (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
