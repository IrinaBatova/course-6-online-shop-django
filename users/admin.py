from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Указываем, какие колонки показывать в списке пользователей
    list_display = ('id', 'email', 'is_staff', 'is_superuser', 'is_active')
