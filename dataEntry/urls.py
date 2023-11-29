from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "dataEnrty"

urlpatterns = [
    path('', clientListView.as_view(), name=''),
    path('clientList/', clientListView.as_view(), name='list'),
    path('create/', clientCreateView.as_view(), name='create'),
    # path('profile/', profile, name='customProfile')
    ]