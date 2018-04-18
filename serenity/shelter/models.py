from __future__ import unicode_literals

from django.db import models
from clients.models import State, Clients

class BedSize(models.Model):
    bedsize_id = models.AutoField(primary_key=True)
    bedsize_description = models.CharField(max_length=20)

    def __str__(self):
        return self.bedsize_description


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_description = models.CharField(max_length=50)

    def __str__(self):
        return self.status_description


class Shelter(models.Model):
    shelter_id = models.AutoField(primary_key=True)
    shelter_name = models.CharField(max_length=200)
    shelter_address_1 = models.CharField(max_length=200, null=False)
    shelter_adddress_2 = models.CharField(max_length=200, null=False)
    shelter_city = models.CharField(max_length=200, null=False)
    shelter_state = models.ForeignKey(State, default=24, related_name='physical_state')
    shelter_zip = models.CharField(max_length=10)
    mailing_address_1 = models.CharField(max_length=200, null=False)
    mailing_adddress_2 = models.CharField(max_length=200, null=False)
    mailing_city = models.CharField(max_length=200, null=False)
    mailing_state = models.ForeignKey(State, default=24, related_name='mailing_state')
    mailing_zip = models.CharField(max_length=10)
    date_opened = models.CharField(max_length=15)
    shelter_status = models.ForeignKey(Status)
    date_closed = models.CharField(max_length=15, null=True, blank=True, default=None)

    def __str__(self):
        return self.shelter_name


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=5)
    room_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    shelter_id = models.ForeignKey(Shelter)
    max_occupancy = models.CharField(max_length=3)
    floor_location = models.CharField(max_length=3)

    def __str__(self):
        if self.room_name:
            return self.room_name
        else:
            return self.room_number


class Bed(models.Model):
    bed_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, related_name='beds')
    bed_size = models.ForeignKey(BedSize)
    client_assigned = models.ForeignKey(Clients, null=True, blank=True, default=None, unique=True)
