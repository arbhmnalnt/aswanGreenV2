from django.urls import path, include
from .views import *

app_name = "collect"

urlpatterns = [
    path('followList/', followsListView.as_view(), name='list'),
    #path('summary/', summary.as_view(), name='summary'),
    path('api/new_colect_order/', NewCollectOrderAPI.as_view()),
    ]