from django.db import models


class Amenity(models.Model):

    """ Amenity Definition"""

    class Meta:
        db_table = 'amenity'
        verbose_name = 'Amenity'
        verbose_name_plural = 'Amenities'

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)