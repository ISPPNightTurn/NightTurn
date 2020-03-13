# Generated by Django 3.0.4 on 2020-03-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0019_auto_20200313_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qr_item',
            old_name='private_key',
            new_name='priv_key',
        ),
        migrations.AlterField(
            model_name='profile',
            name='funds',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
