from django.shortcuts import render
from django.http import HttpResponse

# testing a simple view
def index(request):
	return HttpResponse("This is a test")

