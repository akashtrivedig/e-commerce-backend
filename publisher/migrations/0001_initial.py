# Generated by Django 4.0.2 on 2022-02-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublisherAuth',
            fields=[
                ('contact', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]