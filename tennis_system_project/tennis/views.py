from django.shortcuts import render
from django.http import HttpResponse

# testing a simple view
def index(request):
	context_dict = {'boldmessage': "Here's a message"}
	return render(request, 'tennis/index.html', context=context_dict)

def about(request):
	return HttpResponse("This is an about page <br/> <a href='/tennis/'> Home </a>")

