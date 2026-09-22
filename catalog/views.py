from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, Contacts
from catalog.forms import ProductForm
# from django.core.paginator import Paginator  # Импортируем пагинатор
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from django.urls import reverse_lazy, reverse


class ProductListView(ListView):
    """Контроллер для отображения домашней страницы."""
    model = Product  # Указываем, из какой модели брать данные
    template_name = 'catalog/home.html'  # Путь к HTML-шаблону страницы
    context_object_name = 'products'  # Имя переменной, которая будет использоваться в HTML
    paginate_by = 4  # Пагинация по 4 товара на страницу одной строчкой!

    def get_queryset(self):
        # Переопределяем метод, чтобы товары выводились от новых к старым
        return Product.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        # Получаем базовый контекст, который готовит сам Django (сюда входит и пагинация)
        context = super().get_context_data(**kwargs)

        # Добавляем кастомный код, возвращаем код для вывода в консоль PyCharm
        latest_products = Product.objects.all().order_by('-pk')[:5]

        print("\n--- ПОСЛЕДНИЕ 5 ПРОДУКТОВ ---")
        for product in latest_products:
            print(f"Товар: {product.name} | Цена: {product.price}")
        print("-----------------------------\n")

        # Обязательно возвращаем контекст дальше
        return context


# noinspection PyMethodMayBeStatic
class ContactsView(View):
    """Контроллер для отображения страницы контактов и обработки формы."""

    def get(self, request):
        """Метод обрабатывает обычную загрузку страницы контактов (GET-запрос)"""
        contact_info = Contacts.objects.first()
        context = {
            'contact_info': contact_info
        }
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        """Метод обрабатывает отправку формы пользователем (POST-запрос)"""
        # 1. Снова берём контакты из базы, чтобы страница не сломалась при перезагрузке
        contact_info = Contacts.objects.first()

        # 2. Получаем данные из оригинальной HTML-формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # 3. Выводим полученные данные в консоль PyCharm
        print(f"\nНовое обращение!\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}\n" + "-" * 20)

        # 4. Готовим контекст с флагом успешной отправки
        context = {
            'contact_info': contact_info,
            'success': True
        }
        return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    """ Контроллер для отображения страницы с подробной информацией о товаре."""
    model = Product  # Указываем, из какой модели брать данные
    template_name = 'catalog/product_detail.html'  # Путь к HTML-шаблону страницы товара
    context_object_name = 'product'  # Имя переменной, которая будет использоваться в HTML


class ProductCreateView(CreateView):
    """Контроллер для отображения страницы создания нового товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    # Указываем, куда перенаправить пользователя после успешного создания товара
    success_url = reverse_lazy('catalog:home')

class ProductUpdateView(UpdateView):
    """Контроллер для отображения страницы редактирования товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    # Указываем, куда перенаправить пользователя после успешного редактирования товара
    # success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        # Динамически перенаправляем на детальную страницу только что отредактированного товара
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})