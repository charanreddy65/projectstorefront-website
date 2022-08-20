from django.shortcuts import render,redirect
from django.http import HttpResponse
from projectstorefront.models import Contact, Online_Shoping



# def home(request):
#     return HttpResponse("THIS IS DJANGO PROJECT")

def home(request):
    return render(request,"base.html")

def demo(request):
    if request.method=='POST':
        name = request.POST['myName']
        email = request.POST['myEmail']
        phone = request.POST['myPhone']
        # image = request.FILES.get('myimage')

        k = Contact(name=name,email=email,phone=phone)
        k.save()
        return redirect("food")
    return render(request,"contact.html")

def food(request):
    # online=Online_Shoping.objects.all()
    return render(request,"store.html")

