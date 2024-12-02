# Generated by Django 5.0 on 2024-05-10 21:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_delete_userstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='userstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.FloatField()),
                ('age', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('allergies', models.CharField(max_length=50)),
                ('activity_level', models.FloatField()),
                ('Work_Out_Level', models.CharField(choices=[('intermediate', 'intermediate'), ('Beginner', 'Beginner'), ('Advanced', 'Advanced')], max_length=50)),
                ('fitness_goals', models.CharField(choices=[('Gain weight', 'Gain weight'), ('Healthy Lifestyle', 'Healthy Lifestyle'), ('Lose Weight', 'Lose Weight')], max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('picture', models.ImageField(upload_to=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='state', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
