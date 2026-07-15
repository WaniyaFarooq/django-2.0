from django.shortcuts import render

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data =request.POST
        rn = data.get("receipe_name")
        rd = data.get("receipe_description")
        print(rn)
        print(rd)
    return render(request,"receipes/receipes.html")


