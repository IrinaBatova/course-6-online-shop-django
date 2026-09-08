from django.shortcuts import render
from catalog.models import Product, Contacts


# def home(request):
#     """Контроллер для отображения домашней страницы."""
#     return render(request, 'catalog/home.html')

def home(request):
    """Контроллер для отображения домашней страницы."""
    # Выбираем последние 5 созданных продуктов
    # Минус перед 'pk' (Primary Key / ID) сортирует от самых новых к старым, а [:5] берет первые 5 штук
    latest_products = Product.objects.all().order_by('-pk')[:5]

    # Выводим их в консоль PyCharm циклом
    print("\n--- ПОСЛЕДНИЕ 5 ПРОДУКТОВ ---")
    for product in latest_products:
        print(f"Товар: {product.name} | Цена: {product.price}")
    print("-----------------------------\n")

    return render(request, template_name='catalog/home.html')

def contacts(request):
    """Контроллер для отображения страницы контактов и обработки формы."""
    # 2. Берем первую созданную запись из базы данных
    contact_info = Contacts.objects.first()

    # 3. Кладём её в context, чтобы шаблон её увидел
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
