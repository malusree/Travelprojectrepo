# from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method== 'POST':
        Username=request.POST['username']
        fname= request.POST['first_name']
        lname= request.POST['last_name']
        email= request.POST['email']
        password= request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"username Taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,first_name=fname,last_name=lname,email=email,password=password)
                user.save();
                return redirect('login')
            # print("user created")
        else:
            messages.info(request,"pasword not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')