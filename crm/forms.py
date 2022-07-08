from .models import Client , ClientWallet
from django import forms

class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['created', 'updated']
        widgets = {
            'cid': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_code': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClientWalletForm(forms.ModelForm):

    class Meta:
        model = ClientWallet
        fields = ['available_balance', 'lien_balance' ]
        widgets = {
            'available_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'lien_balance': forms.NumberInput(attrs={'class': 'form-control'}),
        }

       