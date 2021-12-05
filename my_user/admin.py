from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'url', 'image', 'password')}),
        (_('Personal info'), {'fields': ('name', 'locale')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'url', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'url', 'locale', 'is_staff', 'is_active')
    search_fields = ('email', 'name', 'url', 'locale', 'is_active')
    ordering = ('id',)
