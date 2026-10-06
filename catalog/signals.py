from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_product_moderator_group(sender, **kwargs) -> None:
    """Создаёт группу модераторов и назначает права на товары."""
    if sender.name != "catalog":
        return

    group, _ = Group.objects.get_or_create(
        name="Модератор продуктов",
    )

    permissions = Permission.objects.filter(
        content_type__app_label="catalog",
        content_type__model="product",
        codename__in=(
            "change_product",
            "can_unpublish_product",
        ),
    )
    group.permissions.set(permissions)