from django.contrib import admin
from rooms.models import Room


@admin.action(description="Set all prices to 0")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = [
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
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

    search_fields = (
        "=owner__username",  # exact match
        "^price",  # starts with
        "name",  # contains
    )
