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
       # winter season, 31st March
       ageup1 = date(3, 31)
       # summer season 31st August
       ageup2 = date(8, 31)
       # if todays month is between september and march
       # calculate age on March 31st
       # if month is april to august, 
       # calculate age on 31st august
       if (today.month>=9 or today.month<=3):
          age1 = today.year-dob.year-((ageup1.month, ageup1.day) < (dob.month, dob.day))
       elif (today.month>=4 and today.month<=9):
          age2 = today.year-dob.year-((ageup2.month, ageup2.day) < (dob.month, dob.day)) 
       #age = today.year-dob.year-((today.month, today.day) < (dob.month, dob.day))
       if ((age1>=5 and age1<=7) and (age2>=5 and age2<=7)):
          return "red"
       elif ((age1>=8 and age1<=9) or (age2>=8 and age2<=9)):
          return "orange"
       elif (age1>=10 or age2>=10):
          return "green"

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


    
