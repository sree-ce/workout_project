
from django.shortcuts import render

from admins.models import Programs

from .serializers import ProgramSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProgramViewset(viewsets.ModelViewSet):
    queryset = Programs.objects.all()
    serializer_class  = ProgramSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
