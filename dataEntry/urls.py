from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "dataEnrty"

urlpatterns = [
    path('clientList/', clientListView.as_view(), name='list'),
    # path('login/', login, name='customLogin'),
    # path('profile/', profile, name='customProfile')
    ]