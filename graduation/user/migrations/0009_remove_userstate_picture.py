# Generated by Django 5.0 on 2024-05-10 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_userstate_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstate',
            name='picture',
        ),
    ]