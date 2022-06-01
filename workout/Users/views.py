from django.shortcuts import render
from trainers.models import Workouts
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import SubscripitionSerializer
from Users.models import Subscription

class SubscriptionView(viewsets.ModelViewSet):

    queryset = Subscription.objects.all()
    serializer_class = SubscripitionSerializer



class SubscriptionByStatus(viewsets.ModelViewSet):
    
   def get(self, request, is_done):
       customer = Subscription.objects.filter(is_done=is_done)
       if customer:
           serializer = SubscripitionSerializer(customer, many=True)
           return Response(status=200, data=serializer.data)
       return Response(status=400)