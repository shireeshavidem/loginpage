
from django.shortcuts import redirect, render,HttpResponse
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
        if pass1!=pass2:
            
            return HttpResponse("password and conform password are not matching")
        else:
            user = Register(username=eusername,email=email,password1=pass1)
            user.save()
            return redirect('login')
    else:   
        return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        user_det = Register.objects.all()
        user = None
        for i in user_det:
            if (i.username,i.password1)==(username,password):
                user = i.username
                request.method = ""
                break
        if user is not None:
            return redirect('home')
        else:
            return HttpResponse("username or password is wrong")
         
    return render (request,'login.html')

def LogoutPage(request):
    if request.method == 'POST':
        return redirect('login')
    return redirect(request,'home.html')