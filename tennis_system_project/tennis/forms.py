from django import forms
from django.contrib.auth.models import User
from tennis.models import Player, Camp, Day, Session, Attendance, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
   class Meta:
       model = UserProfile
       fields = ('emergcon1', 'emergcon2')

class PlayerForm(forms.ModelForm):
   fname = forms.CharField(max_length=30)
   sname = forms.CharField(max_length=30)
   medicalcons = forms.CharField(max_length=128)
   btmno = forms.IntegerField()
   dob = forms.DateField()

   class Meta:
      model = Player
      # exclude foreign key field
      exclude = ('person',)
