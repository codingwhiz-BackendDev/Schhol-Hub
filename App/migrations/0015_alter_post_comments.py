# Generated by Django 5.0 on 2024-04-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
