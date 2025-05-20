from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'contact_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'contact_number')}),
    )
    list_display = ('username', 'email', 'user_type', 'contact_number', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'user_type', 'contact_number')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
