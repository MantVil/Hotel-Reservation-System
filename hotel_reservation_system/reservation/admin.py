from django.contrib import admin
from reservation.models import Hotel, Reservation

class HotelAdmin(admin.ModelAdmin):
    fields = ['name', 'address']

class ReservationAdmin(admin.ModelAdmin):
    fields = ['hotel', 'check_in_date', 'check_out_date', 'num_guests']

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Reservation, ReservationAdmin)
