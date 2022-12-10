from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomCategory(models.Model):
    CATEGORY_CHOICES = [
        ('KNG', 'King Room'),
        ('DBL', 'Double Room'),
        ('TPL', 'Triple Room'),
        ('QDR', 'Quad Room'),
        ('STE', 'Suite'),
    ]

    name = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    max_occupacy = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, related_name ='reservations', default=None)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.IntegerField()

    def clean(self):
        for room_category in RoomCategory.objects.all():
            if self.room_category.name == room_category.name and self.num_guests > room_category.max_occupacy:
                raise ValidationError(f"Cannot have more than {room_category.max_occupacy} guests in a {room_category.name} room")

    def __str__(self):
        return f'Reservation at {self.hotel.name} {self.room_category.name} from {self.check_in_date} to {self.check_out_date}'
