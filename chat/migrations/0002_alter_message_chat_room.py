# Generated by Django 4.1 on 2022-08-22 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chat.chatroom'),
        ),
    ]
