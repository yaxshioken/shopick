from django.db.models.signals import post_save
from django.dispatch import receiver

from shopick.models import Profile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
