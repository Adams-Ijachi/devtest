from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render , redirect , get_object_or_404
from .models import Client , ClientWallet
from .forms import ClientForm , ClientWalletForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .serializers import ClientSerializer
from rest_framework import generics
# Create your views here.

def home(request, *args, **kwargs):
    clients = Client.objects.all()
    return render(request, 'home.html', {
        'clients': clients
    })
    
def createClient(request):
    form =  ClientForm()
    if request.method == 'POST':  
        form =  ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Created')
            redirect('create_client')

    return render(request, 'create.html', {'form':form})
  
def updateClient(request,pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':  
        form =  ClientForm(request.POST , instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client Updated')
            redirect('update_client' , pk=pk)

    return render(request, 'edit.html', {'form':form})

def deleteClient(request,pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client Deleted')
        return redirect('home')
    
def viewClientWallet(request,pk):
    client = get_object_or_404(Client, pk=pk)
    try:
        form = ClientWalletForm(instance=client.clientwallet)
        if request.method == 'POST': 
            form =  ClientWalletForm(request.POST , instance=client.clientwallet)

            if form.is_valid():
                form.client = client
                form.save()

                redirect('view_client', pk=pk)

    except ObjectDoesNotExist:
        clientWallet = ClientWallet.objects.create(client=client, total_balance=0.00)

    form = ClientWalletForm(instance=client.clientwallet)
    
    return render(request, 'view.html', {'client':client, 'form':form })

class ClientDetailAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
