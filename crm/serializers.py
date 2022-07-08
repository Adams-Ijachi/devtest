from rest_framework import serializers
from .relations import ClientWalletPublicSerializer
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    clientwallet = ClientWalletPublicSerializer(read_only=True)
    class Meta:
        model = Client
        fields = [
                'id', 
                'cid',
                'first_name',
                'last_name',
                'country_code',
                'email',
                'address',
                'phone',
                'clientwallet'
                ]