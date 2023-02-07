from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """Room Model Definition"""

    class Meta:
        db_table = 'rooms'
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms"
    )
    amenities = models.ManyToManyField("rooms.amenity")

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def total_amenities(self):
        return self.amenities.count()

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "No Reviews"
        total_rating = 0
        for review in room.reviews.all().values("rating"):
            total_rating += review["rating"]
        return round(total_rating / count, 2)

    def __str__(self) -> str:
        return self.name
