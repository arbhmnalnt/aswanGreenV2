from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = "dataEntry"

urlpatterns = [
    path('', clientListView.as_view(), name=''),
    path('clientList/', clientListView.as_view(), name='list'),
    path('create/', clientCreateView.as_view(), name='create'),
    path('create2/<int:pk>', contractCreateView.as_view(), name='create_contract')
    # edit or update views
    path('update/', clientCreateView.as_view(), name='create'),
    # path('profile/', profile, name='customProfile')
    ]