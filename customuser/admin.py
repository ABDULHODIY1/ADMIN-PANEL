from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'telegram_id')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'telegram_id')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telegram_id',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
