# Generated by Django 5.0 on 2024-06-06 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_genai_data_alter_genai_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='genai',
            new_name='gen_ai',
        ),
    ]
