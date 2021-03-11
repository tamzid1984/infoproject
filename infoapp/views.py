from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import models
from .models import *
# Create your views here.



def user_login(request):

    if request.method=='POST':
        username=request.POST['uname1']
        password=request.POST['pwd1']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('/home-page')

    return render(request,'user_login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def home_page(request):
    print('hello')
    pbs=PbsInfo.objects.all()
    print('hello1')
    context={'pbs_info':pbs}
    return render(request,'home_page.html',context)

def loged_user(request):
    user=request.user
    context={'user':user}
    return render(request, 'base.html',context)

def pbs_info(request):
    
    return render(request, 'home_page.html',context)

def change_password(request):
    if request.method=='POST':
        old_pass=request.POST['op']
        new_pass=request.POST['np']
        re_type_pass=request.POST['rp']
        user = authenticate(username = request.user.username, password = old_pass)
        if user:
            if new_pass==re_type_pass:
                user = request.user
                print(user)
                user.set_password(new_pass)
                user.save()
                msg1="Password Successfully Changed"
                context={'msg1':msg1}
                return render(request, 'user_login.html',context)
            else:
                msg="New Password and Re-type password not Match"
                context={'msg':msg}
                return render(request, 'change_password.html',context)
        else:
            msg2="Old Password Invalid"
            context={'msg2':msg2}
            return render(request, 'change_password.html',context)
    return render(request, 'change_password.html')
    



