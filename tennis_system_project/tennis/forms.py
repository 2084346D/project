from django import forms
from django.contrib.auth.models import User
from tennis.models import Player, Event, Day, Session, Attendance, UserProfile
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
   class Meta:
       model = UserProfile
       fields = ('emergcon1', 'emergcon2')
       labels = {
          'emergcon1': ('Emergency Contact Number'),
          'emergcon2': ('Emergency Contact Number 2')
       }

       def clean(self):
        if emergcon1[:1] != '0' or '+':
           raise ValidationError(
               _('%(emergcon1)s is not a valid phone number'),
               params={'emergcon1': emergcon1},
           )
        if emergcon2[:1] != '0' or '+':
           raise ValidationError(
               _('%(emergcon2)s is not a valid phone number'),
               params={'emergcon2': emergcon2},
           )

class PlayerForm(forms.ModelForm):
   fname = forms.CharField(max_length=30, label='First Name*')
   sname = forms.CharField(max_length=30, label='Surname*')
   medicalcons = forms.CharField(max_length=500, label='Medical Conditions*')
   btmno = forms.IntegerField(label='BTM Number', required=False)
   dob = forms.DateField(widget=SelectDateWidget(years=range(1917, 2013)), label='Date of Birth*')

   class Meta:
      model = Player
      # exclude foreign key field
      exclude = ('person',)
   
   def clean_btmno(self):
      return self.cleaned_data['btmno'] or None

class EventForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), required=True, label='Event')

    class Meta:
        model = Attendance
        exclude = ('player',)

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('eName',)
        labels = {
           'eName': ('Event Name')
        }
