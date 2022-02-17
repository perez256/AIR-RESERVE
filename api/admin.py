from django.contrib import admin

# Register your models here.
from api.models import Customer, Flight, Booking

admin.site.register(Customer)
admin.site.register(Flight)
admin.site.register(Booking)

