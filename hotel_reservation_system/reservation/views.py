from django.shortcuts import render
from reservation.models import Hotel, Reservation
from rest_framework import generics

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

