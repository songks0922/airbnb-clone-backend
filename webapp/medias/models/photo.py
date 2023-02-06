from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    """ Photo Model Definition """

    class Meta:
        db_table = 'photo'
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    file = models.ImageField()
    description = models.CharField(max_length=80)
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return "Photo File"
