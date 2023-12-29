
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from .models import Registration
# Create your views here.

def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save
        return redirect('login')
    else: 
        form = Registration()  
    return render (request,'signup.html',{'form':form})

def LoginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            return redirect ('home')
    else:
        return render (request,'login.html')

def LogoutPage(request):
    return redirect(request,'login.html')