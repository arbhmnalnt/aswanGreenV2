from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from clientManager.models import *
from django.db.models import Q
from clientManager.forms import *



class clientUpdateView(CreateView):
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
    model = Client
    template_name = 'dataEntry/client_list.html'  
    context_object_name = 'clients'  
    # paginate_by = 100
    queryset = Client.objects.all()  

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query.rstrip()) 
                | Q(serial__icontains=search_query.rstrip())
                | Q(place__name__icontains=search_query.rstrip())
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset =  self.get_queryset()
        # Add additional variable to context
        context['total_count'] = queryset.count()

        return context