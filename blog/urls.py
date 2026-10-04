from django.urls import path
from .views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = 'blog' # Это имя пространства имен для шаблонов

urlpatterns = [
    # Статический маршрут для главной страницы блога (список статей) по адресу /blog/
    path('', BlogPostListView.as_view(), name='list'),
    # Статический маршрут для страницы создания статьи по адресу /blog/create/
    path('create/', BlogPostCreateView.as_view(), name='create'),
    # Динамический маршрут для страницы просмотра одной статьи (например по адресу /blog/1/)
    path('<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    # Динамический маршрут для страницы редактирования одной статьи (например по адресу /edit/1/)
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    # Динамический маршрут для страницы удаления одной статьи (например по адресу /delete/1/)
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]
