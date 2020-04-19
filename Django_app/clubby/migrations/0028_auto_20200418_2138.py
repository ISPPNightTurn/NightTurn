# Generated by Django 3.0.3 on 2020-04-18 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0027_auto_20200418_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_item',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 21, 38, 58, 970310)),
        ),
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 21, 38, 58, 970310)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 21, 38, 58, 969311)),
        ),
        migrations.AlterField(
            model_name='securityadvice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 21, 38, 58, 970310)),
        ),
    ]
