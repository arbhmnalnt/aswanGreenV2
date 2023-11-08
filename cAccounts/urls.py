from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "cAccounts"

urlpatterns = [
    path('logout/', logout, name='customLogout'),
    path('login/', login, name='customLogin'),
    path('profile/', profile, name='customProfile')
    ]