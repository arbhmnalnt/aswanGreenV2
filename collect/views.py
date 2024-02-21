from django.http import HttpResponseRedirect, HttpResponse
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
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.db import transaction




@method_decorator(csrf_exempt, name='dispatch')
class NewCollectOrderAPI(ListView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        selected_clients = data.get('clients', [])
        print(f"selected_clients => {type(selected_clients)}")
        serial = data.get('serial')
        start_collect_date = data.get('startCollectDate')
        collector_id = data.get('collectorId')

        # Validate data (add necessary validation based on your requirements)
        # ...

        # Create CollectOrder and update related objects
        with transaction.atomic():
            collect_request = CollectRequest.objects.create(
                daftrSerial=serial,
                startDate=start_collect_date,
                collector=Employee.objects.get(pk=collector_id),
            )
            selected_clients_chunks = [selected_clients[i:i+100] for i in range(0, len(selected_clients), 100)]
            for chunk in selected_clients_chunks:
                # Assuming selected_clients are client IDs
                clients = Client.objects.filter(pk__in=chunk)
                collect_request.clientt.add(*clients)

        # Handle success response
        response_content = "Collect order created successfully"
        response = HttpResponse(response_content, content_type='text/plain')
        return response



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