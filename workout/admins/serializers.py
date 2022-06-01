from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from admins.models import Programs

class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Programs
        fields = "__all__"