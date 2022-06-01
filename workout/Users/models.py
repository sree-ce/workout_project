from django.db import models
from accounts.models import Customer, Trainer
from trainers.models import Workouts



class Subscription(models.Model):
    workout = models.ForeignKey(Workouts,on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer,on_delete=models.PROTECT)
    is_done = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
     
        self.is_done = True
        super(Subscription, self).save(*args, **kwargs)

