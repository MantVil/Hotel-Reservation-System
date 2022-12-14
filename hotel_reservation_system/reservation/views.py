from rest_framework import generics, viewsets, authentication, permissions
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Hotel, RoomCategory, Reservation
from .serializers import HotelSerializer, RoomCategorySerializer, ReservationSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes= [permissions.IsAuthenticated]
    def get(self, request, format=None):
        usernames= [user.username for user in User.objects.all()]
        return Response(usernames)

class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RoomCategoryList(generics.ListCreateAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RoomCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ReservationList(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
