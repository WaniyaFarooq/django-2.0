from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data =request.POST
        rn = data.get("receipe_name")
        rd = data.get("receipe_description")
        ri = request.FILES.get("recipe_image")
        
        print(rn)
        print(rd)
        print(ri)
        Receipe.objects.create(
        receipe_name =rn,                 
        receipe_description =rd,
        recipe_image =ri)
        return redirect("/receipes/")
    return render(request,"receipes/receipes.html")


