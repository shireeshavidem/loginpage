from os import uname
from re import U
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        # uname=request.POST.get('username')
        # Uemail=request.POST.get('email')
        # upassword=request.POST.get('password')
        # urepassword=request.POST.get('repeatPassword')
        # my_user=User.objects.create_user(sname,semail,spassword)
        # my_user.save()
        return HttpResponse("User has been created sucessfully!!!")
        print(sname,semail,spassword,srepassword)
    return render (request,'signup.html')

def LoginPage(request):
    return render (request,'login.html')