from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tennis.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

def index(request):
    context_dict = {'boldmessage': "Look at this tennis ball"}
    return render(request, 'tennis/index.html', context=context_dict)

def about(request):
    return render(request, 'tennis/about.html')

def register(request):
    # Boolean value for template
    # changes to True with successful registration
    registered = False

    # if it's POST, process form data
    if request.method == 'POST':
        # attempt to grab info from raw form
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # save form data to database
            user = user_form.save()

            # hash password then update user object
            user.set_password(user.password)
            user.save()

            # save UserProfile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # update registered variable
            registered = True

        else:
            # invalid form, print problems to terminal
            print(user_form.errors, profile_form.errors)

    else:
        # not POST so render blank forms
        user_form = UserForm()
        profile_form = UserProfileForm()

    # render the template
    return render(request, 'tennis/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):

    # if request is POST, try to pull out info
    if request.method == 'POST':
        # gather the supplied user and password
        # obtained from log in form
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if email/password combo is valid
        # User object returned if so
        user = authenticate(username=username, password=password)

        # if we have a user object, details were correct
        # if None (Python absent value) no matching user was found
        if user:
            # check account hasn't been disabled
            if user.is_active:
                # if so log in user
                # return them to home
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # inactive account, don't login
                return HttpResponse("Your account is disabled")

        else:
            # bad log in details
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # request is not POST, display log in form
    else:
        # no context variables so pass blank dictionary
        return render(request, 'tennis/login.html', {})
