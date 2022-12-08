from django.urls import path
from reservation import views

urlpatterns = [
    path('hotels/', views.HotelListView.as_view()),
    path('hotels/<int:pk>', views.HotelDetailView.as_view())

]
