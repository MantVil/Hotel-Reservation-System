from django.urls import path
from reservation import views 
urlpatterns = [
    path('hotels/', views.HotelList.as_view()),
    path('hotel/<int:pk>', views.HotelDetail.as_view()),
    path('hotel/room-categories/', views.RoomCategoryList.as_view()),
    path('hotel/room-categories/<int:pk>', views.RoomCategoryDetail.as_view()),
    path('hotel/reservations/', views.ReservationList.as_view(), name='reservation-list'),
    path('hotel/reservations/<int:pk>/', views.ReservationDetail.as_view()),
    path('user/login/', views.UserListView.as_view(), name='login'),
   
]


