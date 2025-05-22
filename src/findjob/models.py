from django.conf import settings
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    rate_type = models.CharField(max_length=10, choices=[('hr', 'Per Hour'), ('day', 'Per Day')])
    details = models.TextField(blank=True)
    city = models.CharField(max_length=100, default='Quezon')

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('worker', 'job')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.worker} - {self.job} - {self.status}"