from django.db import models

from account.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat_room = models.ManyToManyField(ChatRoom, related_name='member')


class Message(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
