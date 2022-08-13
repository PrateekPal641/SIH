from dataclasses import dataclass
from re import X
import re
from xml.dom import ValidationErr
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytz import country_timezones
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from student.models import studata
from django import forms
from django.contrib.auth.decorators import login_required


def evlogin(request):
    if request.method=="POST":
        username: str =  request.POST['Center_ID']
        password =  request.POST['password']
        password = str(password) 
        print(username)
        print(password)
        
        user =None
        user = authenticate(username=username, password=password)
        if user is not None:
            print("yes")
            if user.is_evaluator==False:
                print("UNAUTHORIZED")
                return HttpResponse("<br><br><center><H1>Unauthorized</h1></center>")
            login(request, user)
            return redirect('/../evaluator/scanqr')
        else:
            msg = 'User is not REGISTERED'
            print(msg)
            messages.info(request,'User is not REGISTERED ')
            return redirect('/../evaluator/') 
    return render(request, "EVALUATOR PAGE\login.html")

def scanqr(request):
    if request.user.is_authenticated:
        # print(request.user.image)
        return render(request, "EVALUATOR PAGE\scan.html")
    else:
        msg = 'Unauthorized'
        print(msg)
        messages.info(request,'UNAUTHORIZED!')
        return redirect('/../evaluator/')


def logev(request):
    logout(request)
    messages.info(request,'Successfully logged out!')
    return redirect('/../evaluator/')
