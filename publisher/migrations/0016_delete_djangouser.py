# Generated by Django 4.0.2 on 2022-02-27 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0015_djangouser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DjangoUser',
        ),
    ]
