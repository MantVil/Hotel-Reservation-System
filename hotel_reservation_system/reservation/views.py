from django.shortcuts import render
from reservation.models import Hotel, Reservation
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, RoomCategory, Reservation
from .serializers import HotelSerializer, RoomCategorySerializer, ReservationSerializer

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomCategoryListView(generics.ListAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer

class RoomCategoryDetailView(generics.RetrieveAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer

class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
