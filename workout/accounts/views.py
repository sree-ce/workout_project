import requests
from django.http.response import JsonResponse
from accounts.serializers import UserRegistration, RegisterSerializerTrainer, TrainerProfileSerializer, ProfileSerializer,  UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework import viewsets
from accounts.models import Customer, Trainer, User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.settings import api_settings
from rest_framework.views import APIView
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.views import APIView

from utils.permission import IsAuthenticatedTrainer, IsAuthenticatedCustomer


class UserResgisterView(APIView):

    def post(self, request):
        serializer = UserRegistration(data=request.data)
        print("xcvbn")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserView(APIView):
    def get(self, request):
        print("sdfghjk")
        users = User.objects.all().order_by('-date_joined')

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# @api_view(['GET','POST'])
# def customer_registration(request):


#     if request.method == 'GET':
#         profile = Customer.objects.all()
#         serializer = RegisterSerializer(profile,many=True)
#         return Response(serializer.data)


#     if request.method == 'POST':
#         serializer = RegisterSerializer(data=request.data)

#         data = {}

#         if serializer.is_valid():
#             account = serializer.save()
#             data['response'] = 'Registration successfull'
#             data['username'] = account.username
#             data['email'] = account.email


#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#         return Response(data,status=status.HTTP_201_CREATED)


# def get_token_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh':str(refresh),
#         'access':str(access)
#     }


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def profile_view(request):

    if request.method == 'GET':

        profile = Customer.objects.all()

        serializer = ProfileSerializer(profile, many=True)

        return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticatedCustomer])
@authentication_classes([JWTAuthentication])
def profile_view_edit(request, pk):

    if request.method == 'GET':

        print(request.user)
        profile = Customer.objects.get(pk=pk)

        return Response(serializer.data)

    if request.method == 'PUT':

        profile = Customer.objects.get(pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def trainer_registration(request):

    if request.method == 'GET':
        profile = Trainer.objects.all()
        serializer = TrainerProfileSerializer(profile, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RegisterSerializerTrainer(data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def Tprofile_view(request):

    if request.method == 'GET':

        profile = Trainer.objects.all()

        serializer = TrainerProfileSerializer(profile, many=True)

        return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticatedTrainer])
@authentication_classes([JWTAuthentication])
def trainer_profile_view(request, pk):

    if request.method == 'GET':

        profile = Trainer.objects.get(pk=pk)

        serializer = TrainerProfileSerializer(profile)
        return Response(serializer.data)

    if request.method == 'PUT':

        profile = Trainer.objects.get(pk=pk)
        serializer = TrainerProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
