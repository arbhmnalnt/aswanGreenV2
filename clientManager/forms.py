from django import forms
from .models import Client, Contract, FollowContractServices

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['serial', 'name', 'phone', 'place', 'street', 'building', 'apart', 'details', 'notes', 'serviceId']
        widget = {
            'serial' : forms.TextInput(attrs={'class': 'input form-control'}),
            'name' : forms.TextInput(attrs={'class': 'input form-control'}),
        }
    

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['clientt', 'servicee', 'notes']

class FollowContractServicesForm(forms.ModelForm):
    class Meta:
        model = FollowContractServices
        fields = ['clientt', 'contractt', 'ecd', 'collcetStatus', 'deservedAmount', 'notes']