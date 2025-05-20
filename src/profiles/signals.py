from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
from session.models import User
# from .models import Profile
from .models import WorkerProfile, EmployerProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'worker':
            WorkerProfile.objects.create(user=instance)
        elif instance.user_type == 'employer':
            EmployerProfile.objects.create(user=instance)
        # Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # instance.profile.save()
    if instance.user_type == "worker":
        WorkerProfile.objects.filter(user=instance).update_or_create(user=instance)
    elif instance.user_type == "employer":
        EmployerProfile.objects.filter(user=instance).update_or_create(user=instance)