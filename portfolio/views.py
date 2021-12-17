from django.shortcuts import render,redirect

# Create your views here.

from .models import Contact

def index(request):
    return render(request,'portfolio.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        msg=request.POST['message']
        print(name,email,phone,msg)
        ins=Contact(name=name,email=email,phone=phone,msg=msg)
        ins.save()
    return redirect('contactus')
