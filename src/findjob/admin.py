from django.contrib import admin
from .models import Job, Application
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'schedule', 'salary')
    search_fields = ('name', 'category')

admin.site.register(Job, JobAdmin)
admin.site.register(Application)