from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_lenght=100)
    address = models.CharField(max_lenght=100)

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.IntegerField()