from django.shortcuts import render
# views main fuctions banani han jo url 
# Create your views here.

from django.http import HttpResponse

def home(request):
    peoples = [
    { 'name':'Waniya Farooq' , 'age':22},
    { 'name':'Nadia Farooq' , 'age':52},
    { 'name':'Muazan Farooq' , 'age':15},
    { 'name':'Fakiha Farooq' , 'age':22}
    ]
    return render(request,"home/index.html",context={'peoples':peoples})
   # return HttpResponse("Hey I am a django ")
# we are suppose to return a html template

def contact(request):
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")

