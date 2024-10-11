from django.db.models.signals import post_save
from django.dispatch import receiver

from shopick.models import Profile, Account


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
