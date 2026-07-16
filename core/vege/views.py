from django.http import QueryDict
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data =request.POST
        rn = data.get("receipe_name")
        rd = data.get("receipe_description")
        ri = request.FILES.get("recipe_image")
        
        Receipe.objects.create(
        receipe_name =rn,                 
        receipe_description =rd,
        recipe_image =ri)
        return redirect("/receipes/")
    Queryset = Receipe.objects.all()
    context = {'receipes' : Queryset}
    return render(request,"receipes/receipes.html",context)


