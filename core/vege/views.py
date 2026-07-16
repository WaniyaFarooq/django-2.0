from django.shortcuts import render

from .models import *

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data =request.POST
        rn = data.get("receipe_name")
        rd = data.get("receipe_description")
        ri = request.FILES.get("receipe_image")
        print(rn)
        print(rd)
        print(ri)
        Receipe.objects.create(
        receipe_name =rn,                 
        receipe_description =rd,
        receipe_image =ri)
    return render(request,"receipes/receipes.html")


