from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LugaresSerializer
from .models import Lugares

# Create your views here.

class LugaresView(viewsets.ModelViewSet):
    serializer_class = LugaresSerializer
    queryset = Lugares.objects.all()