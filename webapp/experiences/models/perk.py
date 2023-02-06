from django.db import models
from common.models import CommonModel


class Perk(CommonModel):
    class Meta:
        db_table = 'perk'
        verbose_name = 'Perk'
        verbose_name_plural = 'perks'

    """What is included on an Experience"""
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=250)
    explanation = models.TextField()

    def __str__(self) -> str:
        return self.name