# Generated by Django 5.0 on 2024-04-02 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_likepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='level',
            new_name='faculty',
        ),
    ]