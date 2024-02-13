from django import forms
from .models import *
from clientManager.models import Client

class CollectRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CollectRequestForm, self).__init__(*args, **kwargs)
        self.fields['clientt'].queryset =   Client.objects.all().order_by('name')

    class Meta:
        model   =   CollectRequest
        fields  =   '__all__'