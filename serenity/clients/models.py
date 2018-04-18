from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.contrib.auth.models import User
from neighborhoodwatch.models import Perps


class Gender(models.Model):
    gender_id = models.AutoField(primary_key=True)
    gender_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.gender_description


class Ethnicity (models.Model):
    ethnicity_id = models.AutoField(primary_key=True)
    ethnicity_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.ethnicity_description


class Demographics (models.Model):
    demographics_id = models.AutoField(primary_key=True)
    demographics_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.demographics_description


class State (models.Model):
    state_id = models.AutoField(primary_key=True)
    state_abbreviation = models.CharField(max_length=2, null=False)
    state_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.state_description

class County (models.Model):
    county = models.AutoField(primary_key=True)
    county_name  = models.CharField(max_length=200, null=False)
    state = models.ForeignKey(State, default=26)
    avenues_support = models.BooleanField(default=0)

    def __str__(self):
        return self.county_name


class Type (models.Model):
    type_id = models.AutoField(primary_key=True)
    type_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.type_description


class AbuseType (models.Model):
    abuse_type_id = models.AutoField(primary_key=True)
    abuse_type_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.abuse_type_description


class CallType (models.Model):
    call_type_id = models.AutoField(primary_key=True)
    call_type_description = models.CharField(max_length=200, null=False)


    def __str__(self):
        return self.call_type_description


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_description = models.CharField(max_length=200, default=None, null=False)
    date_created = models.DateField(default=date.today())


    def __str__(self):
        return self.status_description


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_number = models.CharField(max_length=50, default='0', null=True, blank=True, unique=True)
    client_type = models.ForeignKey(Type, null=False)
    first_name = models.CharField(max_length=200, default=None, null=False)
    middle_init = models.CharField(max_length=1, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=200, default=None, null=False)
    county_of_residence = models.ForeignKey(County, null=False, related_name='county_of_residence')
    gender = models.ForeignKey(Gender, null=False)
    county_of_incident = models.ForeignKey(County, null=False, related_name='county_of_incident')
    abusetype = models.ManyToManyField(AbuseType, blank=True)
    phone_number = models.CharField(max_length=12, default=None, null=False)
    dob = models.DateField(default=None, null=True, blank=True)
    #age = models.IntegerField(null=True, blank=True, default="0")
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    perp_id = models.ForeignKey(Perps)
    perp_relationship = models.CharField(max_length=200, default=None, null=True)
    address_1 = models.CharField(max_length=200, default=None, null=True, blank=True)
    address_2 = models.CharField(max_length=200, default=None, null=True, blank=True)
    city = models.CharField(max_length=200, default=None, null=True, blank=True)
    state = models.ForeignKey(State,default=None, null=True, blank=True)
    date_of_first_contact = models.DateField(default=date.today, null=False)
    emergency_contact_name = models.CharField(max_length=200, default=None, null=True)
    emergency_contact_phone = models.CharField(max_length=12, default=None, null=True)
    ethnicity = models.ForeignKey(Ethnicity, null=False, blank=True)
    demographics = models.ManyToManyField(Demographics, blank=True)
    primary_victim = models.CharField(max_length=200, default=None, null=True)


    def __str__(self):
        return self.last_name + ", " + self.first_name

    #@property
    #def age(self):
        #import datetime
        #dob = self.dob
        #tod = datetime.date.today()
        #client_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
        #return client_age

