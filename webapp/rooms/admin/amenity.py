from django.contrib import admin
from rooms.models import Amenity


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "description",
        "created_at",
        "updated_at",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]
