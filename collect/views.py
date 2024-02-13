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
from .forms import *

class new_colect_order(LoginRequiredMixin, CreateView):
    form_class      =   CollectRequestForm
    template_name   =   'collect/collect_order_form.html'
    success_url     = 'collect:list'


class followsListView(LoginRequiredMixin, ListView):
    queryset = FollowContractServices.objects.all()
    model = FollowContractServices
    template_name = 'collect/follow_list.html'
    context_object_name = 'follows'
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
        details = "عرض قائمة سجل متابعة التعاقدات"
        addTrack(depart, person, details)
        return super().get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_term = self.request.GET.get('search', '')

        if search_term:
            follows = FollowContractServices.objects.filter(
                Q(clientt__name__icontains=search_term) |
                Q(clientt__serial__icontains=search_term) |
                Q(clientt__place__name__icontains=search_term)
            ).order_by('-created_at')
        else:
            follows = FollowContractServices.objects.all()
        context['collectors'] = Employee.objects.all()
        context['follows'] = follows.order_by('clientt__name')
        context['total_count'] = follows.count()  # Use 'total_count' instead of 'totalCount'

        return context