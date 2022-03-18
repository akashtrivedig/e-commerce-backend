# date-created: 17-feb-2022
# usage: all the tables related to the publisher and its shops
# calling function: -

from django.utils import timezone
from django.db import models
from users.models import LocalUser


class Shop(models.Model):
    # primary key
    shopId = models.AutoField(primary_key=True)

    # foreign key
    id = models.ForeignKey(
        LocalUser, on_delete=models.CASCADE, related_name='publisher_shop')

    # other details
    name = models.CharField(max_length=64, null=False)
    pincode = models.CharField(max_length=6, null=False)
    address = models.CharField(max_length=255, default='-')
    ipAddress = models.GenericIPAddressField(default='127.0.0.1', null=False)
    browser = models.CharField(
        max_length=255, null=False, default='localhost:chrome')
    registrationDate = models.DateTimeField(default=timezone.now)

