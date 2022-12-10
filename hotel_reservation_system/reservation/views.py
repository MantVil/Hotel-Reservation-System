from django.shortcuts import render
from reservation.models import Hotel, Reservation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, RoomCategory, Reservation
from .serializers import HotelSerializer, RoomCategorySerializer, ReservationSerializer, UserRegistrationSerializer, UserSerializer

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
    permission_classes =(IsAuthenticated)

class UserRegistrationView(generics.CreateAPIView):
    erializer_class = UserRegistrationSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        user = self.request.user
        password = self.request.data.get('password')

        if password and user.id == self.kwargs['pk']:
            if not user.check_password(password):
                raise ValidationError({'password': 'Incorrect password'})

        serializer.save()

class UserDestroyView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()