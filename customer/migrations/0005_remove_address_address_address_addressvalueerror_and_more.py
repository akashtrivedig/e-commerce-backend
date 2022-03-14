# Generated by Django 4.0.3 on 2022-03-14 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='AddressValueError',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AddField(
            model_name='address',
            name='browser',
            field=models.CharField(default='localhost:chrome', max_length=255),
        ),
        migrations.AddField(
            model_name='address',
            name='ipAddress',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='address',
            name='registrationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='browser',
            field=models.CharField(default='localhost:chrome', max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='ipAddress',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='customerauth',
            name='browser',
            field=models.CharField(default='localhost:chrome', max_length=255),
        ),
        migrations.AddField(
            model_name='customerauth',
            name='ipAddress',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='customerauth',
            name='registrationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='feedback',
            name='browser',
            field=models.CharField(default='localhost:chrome', max_length=255),
        ),
        migrations.AddField(
            model_name='feedback',
            name='ipAddress',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='registrationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ordersummary',
            name='browser',
            field=models.CharField(default='localhost:chrome', max_length=255),
        ),
        migrations.AddField(
            model_name='ordersummary',
            name='ipAddress',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='ordersummary',
            name='registrationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
