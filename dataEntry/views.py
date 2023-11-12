from django.shortcuts import render
from django.views.generic.list import ListView
from clientManager.models import *


# Create your views here.

class clientListView(ListView):
    model = Client
    template_name = 'dataEntry/client_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'clients'  # Default: object_list
    # paginate_by = 100
    queryset = Client.objects.all()  # Default: Model.objects.all()