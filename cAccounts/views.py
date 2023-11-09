# import json
# from django.contrib.auth.models import User
# from logging import exception
# from sre_parse import CATEGORIES
# from unicodedata import category
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect, render
# from rest_framework.response import Response
# from django.urls import is_valid_path, reverse
# from django.views.generic.list import ListView
# from rest_framework.views import APIView
# # from symbol import pass_stmt
# from DataEntry.models import *
# from django.contrib.auth.decorators import login_required
# from datetime import *
# from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
# from django.views import View
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from django.contrib.auth import logout as customLogout
from track.views import addTrack
# Create your views here.


def logout(request):
    customLogout(request)
    return redirect ('/cAccounts/login')

@csrf_exempt
def login(request):
    message = ''
    if request.method == 'POST':
        data2 = request.POST
        username = data2.get('username')
        password = data2.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            auth_login(request, user)
            first_name = request.user.first_name
            print(f'user firs name => ', first_name)
            return redirect('/cAccounts/profile')
            # message = f'Hello {user.username}! You have been logged in'
        else:
            message = 'خطأ بإسم المستخدم أو كلمة السر'
    else:
        message = ''
    ctx = {'msg':message}
    return render(request, './cAccounts/login.html', ctx)

def profile(request):
    
    user = request.user
    request.session.setdefault('group', False)
    print(f"user groups => {user.groups.all()}")

    if user.groups.filter(name="dataEntryAdmin"):
        depart = "تسجيل الدخول كمدخل بيانات"
        person = f"{user.first_name} {user.last_name}"
        details = "تم تسجيل الدخول"
        addTrack(depart, person, details)
        request.session['group'] = "dataEntryAdmin"
        return redirect('/DataEntry/')

    elif user.groups.filter(name="allAdmin"):
        depart = "تسجيل الدخول كمطور"
        person = f"{user.first_name} {user.last_name}"
        details = "تم تسجيل الدخول"
        addTrack(depart, person, details)
        request.session['group'] = "allAdmin"
        return redirect('/track/TrackListView')

    elif user.groups.filter(name="tahsealAdmin"):
        depart = "تسجيل الدخول كمسوؤل تحصيل"
        person = f"{user.first_name} {user.last_name}"
        details = "تم تسجيل الدخول"
        addTrack(depart, person, details)
        request.session['group'] = "tahsealAdmin"
        # print("admin here => ")
        return redirect('/DataEntry/TcurrentCollectOrder/')

    elif user.groups.filter(name="customerService"):
        depart = "تسجيل الدخول كمسئول خدمة عملاء"
        person = f"{user.first_name} {user.last_name}"
        details = "تم تسجيل الدخول"
        addTrack(depart, person, details)
        request.session['group'] = "customerService"
        # print("admin here => ")
        return redirect('/cs/')

    else:
        request.session['group'] = "else"
        msg="user has no group"
        return redirect(f'/cAccounts/erorr_page?={msg}')
