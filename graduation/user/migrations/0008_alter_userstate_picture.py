# Generated by Django 5.0 on 2024-05-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_userstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstate',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
