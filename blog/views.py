from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import BlogPost


class BlogPostCreateView(CreateView):
    """Контроллер для отображения страницы создания статьи."""
    model = BlogPost
    # Указываем, какие поля модели выводить в форму на сайте
    fields = ['title', 'content', 'preview', 'is_published']
    # Указываем путь к HTML-шаблону формы
    template_name = 'blog/blog_form.html'
    # Куда перенаправить пользователя после успешного создания статьи
    success_url = reverse_lazy('blog:list')


class BlogPostListView(ListView):
    """Контроллер для отображения страницы со списком статей."""
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Показываем только опубликованные статьи
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    """Контроллер для отображения страницы со статьёй."""
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # Получаем саму статью из базы данных
        obj = super().get_object(queryset)
        # Увеличиваем счётчик просмотров на 1
        obj.views_count += 1
        # Сохраняем обновлённое количество просмотров в базу данных
        obj.save()
        return obj


class BlogPostUpdateView(UpdateView):
    """Контроллер для отображения страницы для редактирования статьи."""
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']  # Поля, доступные для изменения
    template_name = 'blog/blog_form.html'  # Используем тот же шаблон формы, что и для CreateView

    def get_success_url(self):
        # После редактирования возвращаем пользователя на детальную страницу этой же статьи
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    """Контроллер для отображения страницы для удаления статьи."""
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'  # Шаблон подтверждения удаления
    success_url = reverse_lazy('blog:list')  # После удаления перенаправляем на список всех статей
