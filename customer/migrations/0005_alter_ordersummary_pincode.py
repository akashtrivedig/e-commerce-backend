# Generated by Django 4.0.3 on 2022-03-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_addressvalueerror_address_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersummary',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
    ]