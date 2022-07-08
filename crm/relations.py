from rest_framework import serializers

class ClientWalletPublicSerializer(serializers.Serializer):
    total_balance = serializers.DecimalField(max_digits=20, decimal_places=2 , read_only=True )
    available_balance = serializers.DecimalField(max_digits=20, decimal_places=2 , read_only=True)
    lien_balance = serializers.DecimalField(max_digits=20, decimal_places=2 , read_only=True)