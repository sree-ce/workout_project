from rest_framework import serializers
from trainers.models import Blog, Workouts


class WorkoutSerializer(serializers.ModelSerializer):
    # program_name = serializers.CharField(source = 'program.programs')
    # trainer_name = serializers.ReadOnlyField(source = 'trainer.name')
    class Meta:
        model = Workouts
        exclude = ['created_at','updated_at']

    


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"