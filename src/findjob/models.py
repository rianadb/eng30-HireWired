from django.conf import settings
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    details = models.TextField(blank=True)

class Application(models.Model):
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('worker', 'job')  # Prevent duplicate applications