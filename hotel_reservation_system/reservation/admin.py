from django.contrib import admin
from .models import Hotel, RoomCategory, Reservation

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

@admin.register(RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'hotel', 'max_occupacy']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_category', 'check_in_date', 'check_out_date', 'num_guests']
