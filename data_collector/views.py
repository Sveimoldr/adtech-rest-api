from django.shortcuts import render

from rest_framework import viewsets
from .models import AdData
from .serializers import AdDataSerializer

class AdDataViewSet(viewsets.ModelViewSet):
    queryset = AdData.objects.all()
    serializer_class = AdDataSerializer