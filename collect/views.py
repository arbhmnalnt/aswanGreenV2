from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from clientManager.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Prefetch
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from clientManager.models import *
from datetime import date, datetime
from track.views import addTrack
from django.contrib.auth.mixins import LoginRequiredMixin
import sys

#class new_colect_order(LoginRequiredMixin, CreateView):

class clientListView(LoginRequiredMixin, ListView):
    queryset = Client.objects.all()
    model = Client
    template_name = 'collect/client_list.html'
    context_object_name = 'clients'
    # tracking
    def get(self, request, *args, **kwargs):
        # Extract user information from the request
        if request.session['group'] == "dataEntry_admin":
            depart = "مسئول ادخال بيانات"
        elif request.session['group'] == "admin_all":
            depart = "مطور أو مسئول عام"
        elif request.session['group'] == "tahseal_admin":
            depart  =   "مسئول التحصيل"

        person = request.user.first_name + " " + request.user.last_name
        details = "عرض قائمة سجل العملاء"
        addTrack(depart, person, details)
        return super().get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_term = self.request.GET.get('search', '')

        if search_term:
            clients = Client.objects.filter(
                Q(name__icontains=search_term) |
                Q(serial__icontains=search_term) |
                Q(place__name__icontains=search_term)
            ).order_by('-created_at')
        else:
            clients = Client.objects.all().order_by('-created_at')
        context['clients'] = clients
        context['total_count'] = clients.count()  # Use 'total_count' instead of 'totalCount'

        return context