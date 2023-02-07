from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """ Wishlist Model Definition """

    class Meta:
        db_table = 'wishlist'
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        "rooms.Room",
        related_name="wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self) -> str:
        return f"{self.name}"
