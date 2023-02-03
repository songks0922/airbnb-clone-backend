from django.contrib import admin
from rooms.models import Amenity


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
