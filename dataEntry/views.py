from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from clientManager.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



# Create your views here.

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