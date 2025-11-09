from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # this is a view function that will be called when the user visits the index page
    return HttpResponse("Hello, World!") # this is a response to the request