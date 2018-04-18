from __future__ import unicode_literals

from django.db import models
from clients.models import County, State, Gender, Clients
from datetime import datetime
from django.contrib.auth.models import User


class CallLogType(models.Model):
    call_log_type_id = models.AutoField(primary_key=True)
    call_log_type_description = models.CharField(max_length=50)

    def __str__(self):
        return self.call_log_type_description


class CallLog(models.Model):
    call_log_id = models.AutoField(primary_key=True)
    call_log_type = models.ForeignKey(CallLogType)
    time_of_call = models.TimeField()
    county_of_incident = models.ForeignKey(County, null=False, related_name='call_log_county_of_incident')
    first_name = models.CharField(max_length=200, default=None, null=False)
    middle_init = models.CharField(max_length=1, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=200, default=None, null=False)
    victims_name = models.CharField(max_length=200, default=None, null=False)
    safe_phone_contact = models.CharField(max_length=12, blank=True, null=True)
    safe_call = models.BooleanField(default=0)
    address_1 = models.CharField(max_length=200, default=None, null=True, blank=True)
    address_2 = models.CharField(max_length=200, default=None, null=True, blank=True)
    city = models.CharField(max_length=200, default=None, null=True, blank=True)
    state = models.ForeignKey(State,default=None, null=True, blank=True)
    county_of_residence = models.ForeignKey(County, null=False, related_name='call_log_county_of_residence')
    abusers_name = models.CharField(max_length=200, default=None, null=False)
    abusers_city = models.CharField(max_length=200, default=None, null=False)
    immediate_danger = models.BooleanField(default=0)
    previous_victim_dv = models.BooleanField(default=0)
    dv_when = models.CharField(default=None, blank=True, null=True, max_length=10)
    previous_victim_sa = models.BooleanField(default=0)
    sa_when = models.CharField(default=None, blank=True, null=True, max_length=10)
    children = models.BooleanField(default=0)
    num_children = models.CharField(default=0, max_length=3)
    hear_about_avenues = models.CharField(max_length=200, default=None, null=True)
    callback = models.BooleanField(default=0)
    by_whom = models.ForeignKey(User, related_name='call_back', null=True, default=3)
    call_length = models.IntegerField(default=None, null=False)
    taken_by = models.ForeignKey(User, related_name='call_taken_by')
    nature_of_problem = models.CharField(max_length=200, default=None, null=True)
    previous_client = models.BooleanField(default=0)
    pc_when = models.CharField(default=None, blank=True, null=True, max_length=10)
    client_id = models.ForeignKey(Clients, null=True)
    call_notes = models.TextField(null=True, blank=True)
    children_info = models.CharField(max_length=200, null=True, blank=True)


class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    child_age = models.IntegerField()
    child_gender = models.ForeignKey(Gender)
    call_log_id = models.ForeignKey(CallLog)