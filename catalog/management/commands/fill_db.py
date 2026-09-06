from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Очищает базу данных и загружает тестовые данные из фикстур."

    def handle(self, *args, **kwargs):
        # 1. Очищаем базу данных
        self.stdout.write(self.style.WARNING("Очистка базы данных."))
        # Сначала удаляем продукты, так как они ссылаются на категории
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("База данных успешно очищена."))

        try:
            # 2. Используем функцию call_command, чтобы запустить loaddata из кода
            # Сначала категории, чтобы продуктам было к чему привязаться
            call_command("loaddata", "category_data.json")
            call_command("loaddata", "product_data.json")

            # Выводим сообщение об успехе
            self.stdout.write(self.style.SUCCESS("Данные из фикстур успешно загружены"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при загрузке фикстур: {e}"))