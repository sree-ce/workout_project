from django.shortcuts import render
from accounts.models import User                               
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Message                                                   
from .serializer import MessageSerializer, UserSerializer

# Create your views here.
@api_view(['GET','POST'])                                                      
def user_list(request, pk=None):

    if request.method == 'GET':
        if pk:                                                                      
            users = User.objects.filter(id=pk)              
        else:
            users = User.objects.all()                            
        serializer = UserSerializer(users, many=True, context={'request': request}) 
        return Response(serializer.data)  

    elif request.method == 'POST':
        data = JSONParser().parse(request)           
        serializer = UserSerializer(data=data)        
        if serializer.is_valid():
            serializer.save()                                           
            return Response(serializer.data, status=201)     
        return Response(serializer.errors, status=400)     

@api_view(['GET','POST'])
def message_list(request, sender=None, receiver=None):
  
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


