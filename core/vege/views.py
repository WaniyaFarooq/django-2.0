
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
# login to maintain session

# Create your views here.
@login_required(login_url = "/login/")
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
   
    search = request.GET.get("receipe_search")

    if search:
        Queryset = Queryset.filter(
        receipe_name__icontains=search
        )
    context = {'receipes' : Queryset}
    return render(request,"receipes/receipes.html",context)

@login_required(login_url = "/login/")
def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")
    
@login_required(login_url="/login/")
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
    
def login_page(request):
    if request.method == "POST":
        data = request.POST
        Username = data.get("Username")
        Password = data.get("Password")
        user = User.objects.filter(username = Username)
        if user.exists():
            user = authenticate(username =Username ,password = Password)
            if user is None:
                messages.error(request,"Invalid password")
                return redirect('/login/')
            else:
                login(request,user=user)
                return redirect('/receipes/')
        else:
            messages.error(request,'Invalid Username')
    return render(request, 'receipes/login.html')      
            

def register_page(request):
    if request.method == "POST":
        data = request.POST
        First_name = data.get("First_name")
        Last_name = data.get("Last_name")
        Username = data.get("Username")
        Password = data.get("Password")
        user = User.objects.filter(username = Username)
        if user.exists():
            messages.info(request,"Username already taken")
            return redirect("/register/")
        user = User.objects.create(
         first_name = First_name,
         last_name  =Last_name,
         username = Username 
        )
        user.set_password(Password)
        user.save()
        messages.info(request,"Account created successfully")
        return redirect('/login/')
    
    return render(request,'receipes/register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
    
def get_students(request):
    qs = Student.objects.all()
    return render(request,'receipes/students.html',{'qs':qs})
    