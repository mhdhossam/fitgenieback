# Generated by Django 5.0 on 2024-06-07 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_genai_delete_gen_ai'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
    ]