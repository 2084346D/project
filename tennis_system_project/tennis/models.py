from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

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

    def calc_group(self):
       today = datetime.datetime.now()
       if today.month >= 9:
           season_end = datetime.date(today.year+1,3,31)
       elif today.month <= 3:
           season_end = datetime.date(today.year,3,31)
       else:
           season_end = datetime.date(today.year,8,31)
       age_in_years = season_end.year - self.dob.year
       if self.dob.month > season_end.month:
           age_in_years -= 1

       if age_in_years>=5 and age_in_years<=7:
           return "red"
       elif age_in_years>=8 and age_in_years<=9:
           return "orange"
       elif age_in_years>=10 and age_in_years<=11:
           return "green"
       elif age_in_years>=12:
           return "yellow"
       
  
    group = property(calc_group)

# main event object storing event name
class Event(models.Model):
    eName = models.CharField(max_length=128)
    def __str__(self):
      return self.eName
    def __unicode__(self):
      return str(self)

# object for each day of the linked event, stores the date
# of that day
class Day(models.Model):
    linkEvent = models.ForeignKey(Event, null=True)
    date = models.DateField

# session object, one for each morning and each afternoon
# should this have fks to event and day?
class Session(models.Model):
    day = models.ForeignKey(Day)
    timeofday = models.CharField(max_length=30)

# link table which can generate who is attending the event
# on a given day
class Attendance(models.Model):
    player = models.ForeignKey(Player, null=True)
    event = models.ForeignKey(Event, null=True)


    
