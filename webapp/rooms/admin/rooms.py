from django.contrib import admin
from rooms.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "amenities",
    ]

    # def total_amenities(self, room):
    #     return room.amenities.count()
