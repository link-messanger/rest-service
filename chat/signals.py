from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Member


@receiver(post_save, sender=Member)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
