from django.db import models

from common.models import CommonModel


class Amenity(CommonModel):
    """ Amenity Definition"""

    class Meta:
        db_table = 'amenity'
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
