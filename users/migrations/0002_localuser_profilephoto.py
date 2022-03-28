# Generated by Django 4.0.3 on 2022-03-28 08:38

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='localuser',
            name='profilePhoto',
            field=models.ImageField(default='', upload_to=users.models.imageUpload),
        ),
    ]
