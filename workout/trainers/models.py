from django.db import models
from admins.models import Programs
from accounts.models import Trainer

# Create your models here.

class Workouts(models.Model):
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE,null=True)
    workout = models.CharField(max_length=250)
    programs = models.ForeignKey(Programs,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    video = models.FileField(max_length=30)
    preview = models.FileField(max_length=30)
    diet1 = models.CharField(max_length=250)
    diet2 = models.CharField(max_length=250)
    diet_photo = models.ImageField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.workout
    

     
    class Meta:
        verbose_name_plural = 'workouts'


class Blog(models.Model):
    Blog_Title = models.CharField(max_length=250)
    Content = models.TextField()
    Select_image = models.ImageField()