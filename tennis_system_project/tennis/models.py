from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Person stores first name, surname, email, and 
# emergency contacts
class Person(models.Model):
    fname = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    email = models.CharField(max_length=128)
    emrgcon1 = models.CharField(max_length=128)
    emrgcon2 = models.CharField(max_length=128)

# Player stores which person they're associated with,
# first name, surname, medical info, BTM number and 
# date of birth
class Player(models.Model):
    person = models.ForeignKey(Person)
    fname = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    medicalcons = models.CharField(max_length=128)
    btmno = models.IntegerField()
    dob = models.DateField()

# main camp object storing camp name
class Camp(models.Model):
    name = models.CharField(max_length=128)

# object for each day of the linked camp, stores the date
# of that day
class Day(models.Model):
    camp = models.ForeignKey(Camp)
    date = models.DateField

# session object, one for each morning and each afternoon
# should this have fks to camp and day?
class Session(models.Model):
    day = models.ForeignKey(Day)
    timeofday = models.CharField(max_length=30)

# link table which can generate who is attending the camp
# on a given day
class Attendance(models.Model):
    player = models.ForeignKey(Player)
    session = models.ForeignKey(Session)
    
