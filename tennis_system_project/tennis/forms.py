from django import forms
from django.contrib.auth.models import User
from tennis.models import Person, Player, Camp, Day, Session, Attendance, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
   class Meta:
       model = UserProfile
       fields = ('about',)
