from rest_framework import serializers
from .models import Coins

class CoinsSerializers (serializers.ModelSerializer):
    sender = serializers.CharField(source = 'sender.username')
    receiver = serializers.CharField(source = 'sender.username')
    class Meta:
        model = Coins
        fields = '__all__'