from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('worker', 'Worker'),
        ('employer', 'Employer'),
    )
    username = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    contact_number = models.CharField(max_length=100, blank=True, null=True)

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='session_user_groups',  # Unique related_name
    #     blank=True
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='session_user_permissions',  # Unique related_name
    #     blank=True
    # )

    objects = UserManager()

    def __str__(self):
        return self.username