from django.urls import path, include
from .views import *

app_name = "collect"

urlpatterns = [
    path('collectRequest/<int:pk>', collectRequestDetailView.as_view(), name='collectRequest_detail'),
    path('collectRequest/', collectRequest.as_view(), name='request_list'),
    path('followList/', followsListView.as_view(), name='list'),
    #path('summary/', summary.as_view(), name='summary'),
    path('api/new_colect_order/', NewCollectOrderAPI.as_view()),
    ]