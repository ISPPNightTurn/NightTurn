# Generated by Django 3.0.3 on 2020-03-19 18:11

import clubby.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0023_auto_20200316_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='picture',
            field=models.ImageField(blank=True, default='clubby/static/clubby/images/background.jpg', null=True, upload_to=clubby.models.owner_directory_path),
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, default='clubby/static/clubby/images/event_image.jpeg', null=True, upload_to=clubby.models.event_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='clubby/static/clubby/images/user_img.jpg', null=True, upload_to=clubby.models.user_directory_path),
        ),
    ]
