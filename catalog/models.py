from django.db import models

from config import settings


class Category(models.Model):
    """Модель категории товаров."""
    # Стандартный менеджер записей, делает запросы к БД, создается автоматически, здесь прописан явно для линтеров
    objects = models.Manager()

    # Объявление полей модели (колонок таблицы 'Category' в БД)

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание категории",
    )

    # Внутренний класс настраивает параметры самой модели
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара (продукта)."""
    # Стандартный менеджер записей, делает запросы к БД, создается автоматически, здесь прописан явно для линтеров
    objects = models.Manager()

    # Объявление полей модели (колонок таблицы 'Product' в БД)

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название товара",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание товара",
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        # db_index=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
        related_name="products",
        help_text="Выберите категорию товара",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Укажите цену товара",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name = "Признак публикации"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        blank=True,
        null=True
    )

    # Внутренний класс настраивает параметры самой модели
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "-created_at"]
        # Добавляем кастомное право:
        permissions = [
            ("can_unpublish_product", "Можно отменить публикацию товара")
        ]

    def __str__(self):
        return f"{self.name} (Цена: {self.price})"


class Contacts(models.Model):
    """Модель контакты компании."""
    # Стандартный менеджер записей, делает запросы к БД, создается автоматически, здесь прописан явно для линтеров
    objects = models.Manager()

    # Объявление полей модели (колонок таблицы 'Contacts' в БД)
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")

    # Внутренний класс настраивает параметры самой модели
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"Контакты компании (Тел: {self.phone})"
