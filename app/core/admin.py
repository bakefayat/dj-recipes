from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (_('information'), {'fields': ('email', 'password')}),
        (_('personal'), {'fields': ('name',)}),
        (_('permissions'), {'fields': ('is_superuser', 'is_staff', 'last_login')}),
    )


admin.site.register(models.User, UserAdmin)
