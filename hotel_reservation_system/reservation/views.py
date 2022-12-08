from django.shortcuts import render
from reservation.models import Hotel, Reservation
from rest_framework import generics
from .serializers import HotelSerializer, ReservationSerializer

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = HotelSerializer


class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Reservation.objects.all()
    serializer_class = ReservationSerializer