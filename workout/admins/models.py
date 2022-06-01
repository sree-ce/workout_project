from django.db import models

# Create your models here.
class Programs(models.Model):
    programs = models.CharField(max_length=250)
    images = models.ImageField()

    def __str__(self):
        return self.programs