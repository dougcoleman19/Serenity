from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_description = models.CharField(max_length=200, default=None, null=False)
    date_created = models.DateField(default=date.today())


    def __str__(self):
        return self.status_description

class Perps(models.Model):
    perp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, default=None, null=False)
    middle_init = models.CharField(max_length=1, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=200, default=None, null=False)
    birthdate = models.CharField(max_length=15, default=None, blank=True, null=True)
    date_created = models.CharField(max_length=15, default=None, blank=True, null=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)


    def __str__(self):
        # client_name = client.last_name + ", " + client.first_name
        return self.last_name + ", " + self.first_name