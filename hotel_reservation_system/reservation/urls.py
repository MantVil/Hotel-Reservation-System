# from django.urls import path
# from .views import UserList, UserCreate, UserDetail, HotelList, HotelCreate, HotelUpdate, HotelDetail, HotelDelete, RoomList, RoomCreate, RoomUpdate, RoomDetail, RoomDelete, ReservationList, ReservationCreate, ReservationUpdate, ReservationDetail, ReservationDelete


# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('user/create/', UserCreate.as_view()),
#     path('user/<pk>/', UserDetail.as_view()),
#     path('hotels/', HotelList.as_view()),
#     path('hotels/create/', HotelCreate.as_view()),
#     path('hotels/<pk>/update/', HotelUpdate.as_view()),
#     path('hotels/<pk>/', HotelDetail.as_view()),
#     path('hotels/<pk>/delete/', HotelDelete.as_view()),
#     path('rooms/', RoomList.as_view()),
#     path('room//create/', RoomCreate.as_view()),
#     path('room/<pk>/update/', RoomUpdate.as_view()),
#     path('room/<pk>/', RoomDetail.as_view()),
#     path('room/<pk>/delete/', RoomDelete.as_view()),
#     path('reservations/', ReservationList.as_view()),
#     path('reservation/create/', ReservationCreate.as_view()),
#     path('reservation/<pk>/update/', ReservationUpdate.as_view()),
#     path('reservation/<pk>/', ReservationDetail.as_view()),
#     path('reservation/<pk>/delete/', ReservationDelete.as_view()),
# ]
from django.urls import path
from reservation import views 
urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotel/<int:pk>', views.HotelDetailView.as_view()),
    path('hotel/room-categories/', views.RoomCategoryListView.as_view()),
    path('hotel/room-categories/<int:pk>', views.RoomCategoryDetailView.as_view()),
    path('hotel/reservations/', views.ReservationListView.as_view(), name='reservation-list'),
    path('hotel/reservations/<int:pk>/', views.ReservationDetailView.as_view()),
    path('user/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name = 'user-detail'),
    path('users/<int:pk>/update', views.UserUpdateView.as_view(), name = 'user-update'),
    path('users/<int:pk/delete', views.UserDestroyView.as_view(), name = 'user-destroy'),
    path('user/login/', views.LoginView.as_view(), name='login'),
    path('user/logout/', views.LogoutView.as_view(), name='logout'),
    
]
