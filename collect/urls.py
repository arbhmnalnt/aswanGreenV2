from django.urls import path, include
from .views import *
from dataEntry.views import clientListView

app_name = "collect"

urlpatterns = [
    path('clientList/', clientListView.as_view(), name='list'),
    ]