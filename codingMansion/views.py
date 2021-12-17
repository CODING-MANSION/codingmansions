from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def portfolio(request):
    return render(request,'portfolio.html')

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')


#################### ERROR HANDLER ##############################

def error_404(request,exception):
	return render(request,'error_404.html')



