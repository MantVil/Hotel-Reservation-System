from django.urls import path
from reservation import views

urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotel/<int:pk>', views.HotelDetailView.as_view()),
    path('room-categories/', views.RoomCategoryListView.as_view()),
    path('room-categories/<int:pk>', views.RoomCategoryDetailView.as_view()),
    path('reservations/', views.ReservationListView.as_view()),
    path('reservations/create/', views.ReservationCreateView.as_view()),
]