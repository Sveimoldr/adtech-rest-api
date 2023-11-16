from rest_framework import serializers
from .models import AdData

class AdDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdData
        fields = '__all__'