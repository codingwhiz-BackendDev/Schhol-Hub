# Generated by Django 5.0 on 2024-04-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_rename_level_profile_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Favourites')),
            ],
        ),
    ]
