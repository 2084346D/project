from django.shortcuts import render
from django.http import HttpResponse
from tennis.forms import UserForm, UserProfileForm

def index(request):
	context_dict = {'boldmessage': "Look at this tennis ball"}
	return render(request, 'tennis/index.html', context=context_dict)

def about(request):
	return render(request, 'tennis/about.html')

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'tennis/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})
