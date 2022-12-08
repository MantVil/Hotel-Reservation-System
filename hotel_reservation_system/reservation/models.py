from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.IntegerField()

    def __str__(self):
        return f'Reservation at {self.hotel.name} from {self.check_in_date} to {self.check_out_date}'