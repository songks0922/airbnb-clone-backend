from django.db import models


class House(models.Model):
    '''Model Definition for House'''

    class Meta:
        db_table = 'houses'
        verbose_name = 'House'
        verbose_name_plural = 'Houses'

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
