from django.contrib import admin
from postlog.models import FlightNum,Destination,Parking,DepartureTime,Flight,Airline
# Register your models here.

admin.site.register(FlightNum)
admin.site.register(Destination)
admin.site.register(Parking)
admin.site.register(DepartureTime)
admin.site.register(Flight)
admin.site.register(Airline)
