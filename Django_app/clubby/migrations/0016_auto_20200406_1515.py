# Generated by Django 3.0.4 on 2020-04-06 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0015_auto_20200404_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_item',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 15, 15, 39, 489741)),
        ),
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 15, 15, 39, 489741)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 15, 15, 39, 487729)),
        ),
        migrations.AlterField(
            model_name='securityadvice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 15, 15, 39, 487729)),
        ),
    ]
