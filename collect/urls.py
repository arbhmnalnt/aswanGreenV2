from django.urls import path, include
from .views import *

app_name = "collect"

urlpatterns = [
    path('clientList/', followsListView.as_view(), name='list'),
    #path('summary/', summary.as_view(), name='summary'),
   path('new_colect_order/', new_colect_order),
    ]