from django.db import models

# Create your models here.
class data (models.Model):
    name= models.CharField(max_length=25)
    city = models.CharField(max_length=30)