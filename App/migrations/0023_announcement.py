# Generated by Django 5.0 on 2024-04-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_alter_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='announcement')),
            ],
        ),
    ]
