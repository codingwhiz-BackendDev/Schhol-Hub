# Generated by Django 5.0 on 2024-04-03 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0020_remove_comment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='name',
        ),
    ]
