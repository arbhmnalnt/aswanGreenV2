from django.shortcuts import render
from clientManager.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from clientManager.models import *
from django.db.models import Q
from clientManager.forms import *



class clientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'dataEntry/client_form.html'
    success_url = 'dataEntry:clientList'  # Replace with your actual success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contract_form'] = ContractForm()
        context['follow_contract_form'] = FollowContractServicesForm()
        return context

    def form_valid(self, form, *args, **kwargs):
        response = super().form_valid(form)

        # Create a new Contract instance
        contract_form = ContractForm(self.request.POST)
        if contract_form.is_valid():
            contract = contract_form.save(commit=False)
            contract.clientt = self.object
            contract.save()

            # Create a new FollowContractServices instance
            follow_contract_form = FollowContractServicesForm(self.request.POST)
            if follow_contract_form.is_valid():
                follow_contract = follow_contract_form.save(commit=False)
                follow_contract.clientt = self.object
                follow_contract.contractt = contract
                follow_contract.save()

        return response

    def form_invalid(self, form, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['contract_form'] = ContractForm(self.request.POST)
        context['follow_contract_form'] = FollowContractServicesForm(self.request.POST)
        return self.render_to_response(context)

class clientListView(ListView):
    queryset = Client.objects.all()
    model = Client
    template_name = 'dataEntry/client_list.html'
    context_object_name = 'clients'
    # paginate_by = 10
    # ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_term = self.request.GET.get('search', '')

        if search_term:
            clients = Client.objects.filter(
                Q(name__icontains=search_term) |
                Q(serial__icontains=search_term) |
                Q(place__name__icontains=search_term)
            )
        else:
            clients = Client.objects.all()

        context['clients'] = clients
        context['total_count'] = clients.count()  # Use 'total_count' instead of 'totalCount'

        return context