from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
# from session.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    experience = models.TextField(blank=True)
    details = models.TextField(blank=True)
    contact_number = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='profile_pictures/default.jpg')
    certification = models.FileField(upload_to='certifications/', blank=True, null=True)

    def __str__(self):
        return self.user.username
