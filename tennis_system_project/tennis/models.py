from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    emergcon1 = models.CharField(max_length=128, blank=False)
    emergcon2 = models.CharField(max_length=128, blank=False)

    def _unicode_(self):
        return self.user.username

# Player stores which person they're associated with (via user object),
# first name, surname, medical info, BTM number and 
# date of birth
class Player(models.Model):
    person = models.ForeignKey(User)
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


    
