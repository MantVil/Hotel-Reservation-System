from django.urls import path
from reservation import views

urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotel/<int:pk>', views.HotelDetailView.as_view()),
    path('hotel/room-categories/', views.RoomCategoryListView.as_view()),
    path('hotel/room-categories/<int:pk>', views.RoomCategoryDetailView.as_view()),
    path('hotel/reservations/', views.ReservationListView.as_view()),
    path('hotel/reservations/create/', views.ReservationCreateView.as_view()),
    path('user/register/', views.UserRegistrationView.as_view(), name='user registration'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name = 'user-detail'),
    path('users/<int:pk>/update', views.UserUpdateView.as_view(), name = 'user-update')
]
