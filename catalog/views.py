from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contacts

# def home(request):
#     """Контроллер для отображения домашней страницы."""
#     return render(request, 'catalog/home.html')

def home(request):
    """Контроллер для отображения домашней страницы."""
    # ЗАПРОС ДЛЯ КОНСОЛИ: Выбираем только последние 5 созданных продуктов
    # Минус перед 'pk' (Primary Key / ID) сортирует от самых новых к старым, а [:5] берет первые 5 штук
    latest_products = Product.objects.all().order_by('-pk')[:5]

    # Выводим их в консоль PyCharm циклом
    print("\n--- ПОСЛЕДНИЕ 5 ПРОДУКТОВ ---")
    for product in latest_products:
        print(f"Товар: {product.name} | Цена: {product.price}")
    print("-----------------------------\n")

    # ЗАПРОС ДЛЯ СТРАНИЦЫ: Выбираем ВСЕ товары сортируя их по первичному ключу (pk) в обратном порядке (минус перед
    # pk означает «по убыванию»). Новые товары будут на первом месте.
    all_products = Product.objects.all().order_by('-pk')

    # Кладем ВСЕ товары в контекст шаблона
    context = {
        'object_list': all_products
    }

    # Передаем контекст в шаблон
    return render(request, 'catalog/home.html', context)

def contacts(request):
    """Контроллер для отображения страницы контактов и обработки формы."""
    # Берем первую созданную запись из базы данных
    contact_info = Contacts.objects.first()

    # Кладём её в context, чтобы шаблон её увидел
    context = {
        'contact_info': contact_info
    }

    if request.method == 'POST':
        # Получаем данные из оригинальной HTML-формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')  # Считываем переданный телефон
        message = request.POST.get('message')

        # Выводим полученные данные в консоль PyCharm
        print(f"Новое обращение!\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}\n" + "-" * 20)

        # Передаем флаг успешной отправки для отображения плашки alert
        context['success'] = True

    return render(request, 'catalog/contacts.html', context)

def product_detail(request, pk):
    # Находим товар по его pk (Primary Key).
    # product = Product.objects.get(pk=pk), но лучше использовать get_object_or_404
    # Если товара нет, get_object_or_404 вернет ошибку 404 вместо падения сайта.
    product = get_object_or_404(Product, pk=pk)

    # Формируем контекст для передачи в шаблон (как в лекции)
    context = {
        'product': product
    }

    # Возвращаем ответ с отрендеренным шаблоном
    return render(request, 'catalog/product_detail.html', context)
