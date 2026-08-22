from django.shortcuts import render


def home(request):
    """Контроллер для отображения домашней страницы."""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер для отображения страницы контактов и обработки формы."""
    context = {}

    if request.method == 'POST':
        # Получаем данные из оригинальной HTML-формы курса
        name = request.POST.get('name')
        phone = request.POST.get('phone')  # Считываем переданный телефон
        message = request.POST.get('message')

        # Выводим полученные данные в консоль PyCharm
        print(f"Новое обращение!\nИмя: {name}\nТелефон: {phone}\nСообщение: {message}\n" + "-" * 20)

        # Передаем флаг успешной отправки для отображения плашки alert
        context['success'] = True

    return render(request, 'catalog/contacts.html', context)
