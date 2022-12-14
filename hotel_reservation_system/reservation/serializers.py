from rest_framework import serializers
from .models import Hotel, RoomCategory, Reservation

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'address')

class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = ('id', 'name', 'hotel', 'max_occupacy')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'hotel', 'user', 'room_category', 'check_in_date', 'check_out_date', 'num_guests')
