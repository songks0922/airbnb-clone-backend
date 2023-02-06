from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """ Wishlist Model Definition """

    class Meta:
        db_table = 'wishlist'
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField("rooms.Room")
    experiences = models.ManyToManyField("experiences.Experience")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
