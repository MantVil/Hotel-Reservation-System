from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_lenght=100)
    address = models.CharField(max_lenght=100)
    