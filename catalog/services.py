from django.core.cache import cache
from django.conf import settings
from catalog.models import Product


def get_products_by_category(category_id):
    """
    Сервисная функция для получения списка продуктов в категории.
    Использует низкоуровневое кэширование Redis.
    """
    # Проверяем, включено кэширование в проекте или нет
    if not settings.CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    # Формируем уникальный ключ для этой категории
    cache_key = f'category_{category_id}'

    # Пытаемся достать данные из кэша Redis
    products = cache.get(cache_key)

    # Если в Redis ничего нет (кэш пуст или устарел)
    if products is None:
        # Делаем запрос к базе данных
        products = Product.objects.filter(category_id=category_id)
        # Записываем результат в Redis на 15 минут (900 секунд)
        cache.set(cache_key, products, timeout=60*15)

    return products