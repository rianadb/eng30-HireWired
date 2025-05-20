from django.contrib import admin

# Register your models here.
# from django.contrib.auth.models import User
# from .models import Profile
from .models import WorkerProfile, EmployerProfile
from session.models import User
from session.admin import CustomUserAdmin

class WorkerProfileInline(admin.StackedInline):
    model = WorkerProfile
    can_delete = False
    verbose_name_plural = 'Worker Profiles'

class EmployerProfileInline(admin.StackedInline):
    model = EmployerProfile
    can_delete = False
    verbose_name_plural = 'Employer Profiles'

# Extend the UserAdmin
class UserAdmin(CustomUserAdmin):
    inlines = (WorkerProfileInline, EmployerProfileInline)
    list_display = ('username', 'email', 'first_name', 'last_name')

# # Unregister the default User admin and register the customized one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)