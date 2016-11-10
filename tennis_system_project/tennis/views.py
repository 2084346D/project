from django.shortcuts import render
from django.http import HttpResponse

# testing a simple view
def index(request):
	context_dict = {'boldmessage': "Look at this tennis ball"}
	return render(request, 'tennis/index.html', context=context_dict)

def about(request):
	return render(request, 'tennis/about.html')

