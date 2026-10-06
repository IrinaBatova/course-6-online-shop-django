from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from catalog.models import Product

User = get_user_model()


class ProductAccessTests(TestCase):

    def setUp(self):
        # 1. Создаем пользователей БЕЗ username (используем только email)
        self.owner = User.objects.create_user(
            email="owner@test.com", password="password"
        )
        self.stranger = User.objects.create_user(
            email="stranger@test.com", password="password"
        )
        self.moderator = User.objects.create_user(
            email="moderator@test.com", password="password"
        )

        # Добавляем модератора в группу (она создается автоматически вашим сигналом post_migrate)
        moderator_group = Group.objects.get(name="Модератор продуктов")
        self.moderator.groups.add(moderator_group)

        # 2. Создаем тестовый продукт, владельцем которого является self.owner
        self.product = Product.objects.create(
            name="Тестовый продукт", price=100, owner=self.owner
        )

        # 3. Генерируем URL-адреса для проверки
        self.update_url = reverse(
            "catalog:update_product", kwargs={"pk": self.product.pk}
        )
        self.delete_url = reverse(
            "catalog:delete_product", kwargs={"pk": self.product.pk}
        )

    def test_owner_access(self):
        """Владелец может зайти на редактирование и удаление своего товара."""
        # Для авторизации передаем email вместо username
        self.client.login(email="owner@test.com", password="password")

        response_update = self.client.get(self.update_url)
        self.assertEqual(response_update.status_code, 200)

        response_delete = self.client.get(self.delete_url)
        self.assertEqual(response_delete.status_code, 200)

    def test_stranger_access_denied(self):
        """Посторонний пользователь получает ошибку 403 (Доступ запрещен)."""
        self.client.login(email="stranger@test.com", password="password")

        response_update = self.client.get(self.update_url)
        self.assertEqual(response_update.status_code, 403)

        response_delete = self.client.get(self.delete_url)
        self.assertEqual(response_delete.status_code, 403)

    def test_moderator_access(self):
        """Модератор из группы может изменять и удалять товар."""
        self.client.login(email="moderator@test.com", password="password")

        response_update = self.client.get(self.update_url)
        self.assertEqual(response_update.status_code, 200)

        response_delete = self.client.get(self.delete_url)
        self.assertEqual(response_delete.status_code, 200)
