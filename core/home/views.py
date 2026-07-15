from django.shortcuts import render
# views main fuctions banani han jo url 
# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hey I am a django ")
# we are suppose to return a html template