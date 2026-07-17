

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
    if request.method == "GET":
        search = request.GET.get("search")
        qs = Queryset.filter(receipe_name__icontains = search)
    return render(request,"receipes/receipes.html",context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")
    

def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    context  = {'receipe': queryset}
    if request.method == "POST":
        data =request.POST
        rn = data.get("receipe_name")
        rd = data.get("receipe_description")
        ri = request.FILES.get("recipe_image")
        
        queryset.receipe_name = rn
        queryset.receipe_description = rd
        if ri:
            queryset.recipe_image =ri
        queryset.save()
        # request.POST k through hum hum frontend sy backend main bhejty h
        # contxt k throug backend sy frontend pr
        return redirect("/receipes/")
    return render(request,"receipes/update_receipes.html",context)
    
