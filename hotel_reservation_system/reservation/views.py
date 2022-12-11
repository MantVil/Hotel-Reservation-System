from django.shortcuts import render, get_object_or_404
from reservation.models import Hotel, Reservation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ReservationListView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        
        reservations = Reservation.objects.filter(user=request.user)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class ReservationDetailView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request, pk):
        # Get the reservation with the given ID
        reservation = get_object_or_404(Reservation, pk=pk)

        # Only allow the user to see their own reservation
        if reservation.user != request.user:
            return Response(status=403)

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)

        if reservation.user != request.user:
            return Response(status = 403)
        
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)

        if reservation.user != request.user:
            return Response(status=403)
        
        reservation.delete()
        return Response(status=204)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

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

    def get_object(self):
        return self.request.user

# class LoginView(ObtainAuthToken):
