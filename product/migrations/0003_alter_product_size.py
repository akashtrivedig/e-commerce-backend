# Generated by Django 4.0.3 on 2022-03-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default='abstract', max_length=8, null=True),
        ),
    ]
