from reservation.models import Hotel, Reservation
from rest_framework import serializers

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'address')

    
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'hotel', 'check_in_date', 'check_out_date', 'num_guests')