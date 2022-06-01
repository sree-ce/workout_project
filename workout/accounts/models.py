from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    name = models.CharField(max_length=250)
    
    mobile = models.CharField(unique=True,max_length=250,blank=True)

class Customer(models.Model):
    customer = models.ForeignKey(
        User,on_delete=models.CASCADE, related_name="customer_account"
    )
    age = models.CharField(max_length=250)
    weight = models.IntegerField()
    height = models.IntegerField()
    

    def __str__(self):
        return self.customer.name
    
   

class Trainer(models.Model):
    CERTIFICATES = ( 
        ('ISSA','ISSA'),
        ('NCSF','NCSF'),
        ('ACE','ACE'),
        ('FITNESS MENTORS','fitness mentors'),
        ('PG','PG'),
        ('B.Ed','B.Ed'),
        ('DIPLOMA ','diploma '),
        
    )
    trainer = models.ForeignKey(
        User,on_delete=models.CASCADE,related_name="trainer"
    )
    certification = models.CharField(max_length=250,choices=CERTIFICATES)
    stream = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.trainer.name

