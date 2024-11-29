from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile instance when a new User is created.
    Checks if a Profile already exists to prevent duplication.
    """
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the Profile instance when the User is saved.
    Ensures profile data is kept in sync.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
