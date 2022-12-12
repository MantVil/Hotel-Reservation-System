from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Hotel, RoomCategory, Reservation
from .serializers import UserSerializer, HotelSerializer, RoomSerializer, ReservationSerializer
from rest_framework import viewsets, generics, mixins, permissions,status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(pk=self.request.user.pk)
        if user.exists():
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('User doesn\'t exist.')

class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HotelCreate(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelUpdate(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDelete(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomList(generics.ListAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomSerializer

class RoomCreate(generics.CreateAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomSerializer

class RoomUpdate(generics.UpdateAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomSerializer

class RoomDelete(generics.DestroyAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomSerializer

class ReservationList(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationCreate(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationUpdate(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDelete(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer






# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.core.exceptions import ValidationError
# from rest_framework import generics, status, permissions, authentication
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from .models import Hotel, RoomCategory, Reservation
# from .serializers import HotelSerializer, RoomCategorySerializer, ReservationSerializer, UserRegistrationSerializer, UserSerializer, LoginSerializer


# class HotelListView(generics.ListAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

# class HotelDetailView(generics.RetrieveAPIView):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

# class RoomCategoryListView(generics.ListAPIView):
#     queryset = RoomCategory.objects.all()
#     serializer_class = RoomCategorySerializer

# class RoomCategoryDetailView(generics.RetrieveAPIView):
#     queryset = RoomCategory.objects.all()
#     serializer_class = RoomCategorySerializer

# class ReservationListView(APIView):
#     permission_classes = (IsAuthenticated)

#     def get(self, request):
#         reservations = Reservation.objects.filter(user=request.user)
#         serializer = ReservationSerializer(reservations, many=True)
#         return Response(serializer.data)

# class ReservationDetailView(APIView):
#     permission_classes = (IsAuthenticated)

#     def get(self, request, pk):
#         # Get the reservation with the given ID
#         reservation = get_object_or_404(Reservation, pk=pk)

#             # Only allow the user to see their own reservation
#         if reservation.user != request.user:
#             return Response(status=403)

#         serializer = ReservationSerializer(reservation)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         reservation = get_object_or_404(Reservation, pk=pk)

#         if reservation.user != request.user:
#             return Response(status = 403)
        
#         serializer = ReservationSerializer(reservation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         reservation = get_object_or_404(Reservation, pk=pk)

#         if reservation.user != request.user:
#             return Response(status=403)
        
#         reservation.delete()
#         return Response(status=204)

# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserRegistrationSerializer

# class UserDetailView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

# class UserUpdateView(generics.UpdateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def perform_update(self, serializer):
#         user = self.request.user
#         password = self.request.data.get('password')

#         if password and user.id == self.kwargs['pk']:
#             if not user.check_password(password):
#                 raise ValidationError({'password': 'Incorrect password'})
#         serializer.save()


# class UserDestroyView(generics.DestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def get_object(self):
#         return self.request.user()

# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#     authentication_classes = (authentication.BasicAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         # Generate a new token for the user
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key})


# class LogoutView(APIView):
#     authentication_classes = (TokenAuthentication, BasicAuthentication)
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
