# Generated by Django 5.0 on 2024-04-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]