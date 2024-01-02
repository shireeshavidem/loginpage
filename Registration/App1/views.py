
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from .models import Register
# Create your views here.

def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        eusername=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            
            details = Register(username=eusername,email=email,password1=pass1)
            details.save()
            
            return redirect('login')
    else:   
        return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        user = authenticate(request,username=username,password1=password)
        if user is not None:
           login(request,user)
           return redirect('home') 
        else:
            return None
         
    return render (request,'login.html')

def LogoutPage(request):
    return redirect(request,'login.html')