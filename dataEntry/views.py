from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from clientManager.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from clientManager.models import *
from django.db.models import Q
from clientManager.forms import *
from datetime import date, datetime
from track.views import addTrack
from django.contrib.auth.mixins import LoginRequiredMixin

import sys

class contractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'dataEntry/contract_form.html'

    def get(self, request, *args, **kwargs):
        # Extract user information from the request
        if request.session['group'] == "dataEntry_admin":
            depart = "مسئول ادخال بيانات"
        elif request.session['group'] == "admin_all":
            depart = "مطور أو مسئول عام"

        person = request.user.first_name + " " + request.user.last_name
        details = "انشاء سجل عميل وتعاقد جديد"
        addTrack(depart, person, details)
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        client_record = Client.objects.get(pk=self.kwargs['pk'])
        print(client_record)
        kwargs['initial'] = {'clientt':client_record.pk}
        return kwargs
    
    def form_valid(self, form):
        if self.object:
            print(f"Object is not None. Object type: {type(self.object)}, Object ID: {self.object.id}")
            contract_id     = self.object.pk
            client_id       = self.object.clientt_id 
            contractDate    = self.object.contractDate
            ecd           = get_ecd(contractDate)
            deserved_amount = Service.objects.get(pk=self.object.servicee_id).price
            FollowContractServices.objects.create(
                clientt         =   client_id,
                contract        =   contract_id,
                contractDate    =   contractDate,
                ecd             =   ecd,
                deserved_amount =   deserved_amount
            )
        else:
            print("Object is None. Form was not saved correctly.")
        return HttpResponseRedirect(reverse('dataEntry:list'))
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

class clientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'dataEntry/client_form.html'

    def get_success_url(self):
        created_client = self.object  # Get the newly created client object
        return reverse('dataEntry:create_contract', kwargs={'pk': created_client.pk})

class clientListView(LoginRequiredMixin, ListView):
    queryset = Client.objects.all()
    model = Client
    template_name = 'dataEntry/client_list.html'
    context_object_name = 'clients'
    # tracking
    def get(self, request, *args, **kwargs):
        # Extract user information from the request
        if request.session['group'] == "dataEntry_admin":
            depart = "مسئول ادخال بيانات"
        elif request.session['group'] == "admin_all":
            depart = "مطور أو مسئول عام"

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

# =============     FUNNCTIONS PART ===============

def get_ecd(input_date):
    # Get the current date
    current_date = datetime.now()
    
    # Replace the month in the input_date with the current month
    new_date = input_date.replace(month=current_date.month)
    
    return new_date