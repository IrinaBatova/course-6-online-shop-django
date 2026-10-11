from typing import Any
from catalog.models import Category

def categories_processor(request: Any) -> dict[str, Any]:
    """
    Глобально добавить список всех категорий в контекст всех шаблонов сайта.
    """
    return {
        'categories': Category.objects.all()
    }
