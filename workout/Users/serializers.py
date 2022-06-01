
from rest_framework import serializers

from Users.models import Subscription
from trainers.models import Workouts



class SubscripitionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscription
        fields = "__all__"
