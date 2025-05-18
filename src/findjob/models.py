from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
