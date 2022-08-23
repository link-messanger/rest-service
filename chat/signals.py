from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Member
from chat_app.settings import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
