from django.urls import path
from .apps import BlogConfig
from .views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

# urlpatterns = [
#     # Маршрут для создания статьи (пока без списка статей, его добавим следующим)
#     path('create/', BlogPostCreateView.as_view(), name='create'),
# ]

urlpatterns = [
    # Маршрут для главной страницы блога (список статей) по адресу /blog/
    path('', BlogPostListView.as_view(), name='list'),
    # Маршрут для страницы создания статьи по адресу /blog/create/
    path('create/', BlogPostCreateView.as_view(), name='create'),
    # Маршрут для страницы просмотра одной статьи (например по адресу /blog/1/)
    path('<int:pk>/', BlogPostDetailView.as_view(), name='detail'),
    # Маршрут для страницы редактирования одной статьи (например по адресу /edit/1/)
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    # Маршрут для страницы удаления одной статьи (например по адресу /delete/1/)
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]
