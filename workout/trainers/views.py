import requests
from rest_framework import status
from trainers.models import Blog, Workouts
from trainers.serializers import BlogSerializer, WorkoutSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, parsers, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.permission import IsAuthenticatedTrainer


class WorkoutList(generics.ListCreateAPIView):

    permission_classes = [AllowAny]

    queryset = Workouts.objects.all()

    serializer_class = WorkoutSerializer


    name = 'Workouts'

    filter_fields = (
    	'programs',

    )


class WorkoutDetailView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, pk):
        # request.user
        try:
            workouts = Workouts.objects.get(pk=pk)
        except Workouts.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkoutSerializer(workouts)
        return Response(serializer.data)

    def put(self, request, pk):
        workouts = Workouts.objects.get(pk=pk)
        serializer = WorkoutSerializer(
            workouts, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workouts = Workouts.objects.get(pk=pk)
        workouts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
