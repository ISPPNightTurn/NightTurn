# Generated by Django 3.0.4 on 2020-03-11 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubby', '0009_auto_20200309_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.ManyToManyField(to='clubby.Basket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QR_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_used', models.BooleanField(default=False)),
                ('private_key', models.CharField(max_length=128)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Order')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clubby.Product')),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clubby.Reservation')),
                ('ticket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clubby.Ticket')),
            ],
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='hookah',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='product',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='reservation',
        ),
        migrations.DeleteModel(
            name='Hookah',
        ),
        migrations.DeleteModel(
            name='Receipt',
        ),
    ]
