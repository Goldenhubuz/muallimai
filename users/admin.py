from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html

from shared.admin import BaseAdmin

User = get_user_model()


# Register your models here.

class UserAdmin(BaseAdmin):
    list_display = ['username', 'email', 'is_superuser', 'is_active', 'date_joined']


admin.site.register(User, UserAdmin)