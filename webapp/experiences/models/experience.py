from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    class Meta:
        db_table = 'experience'
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    """Experience Model Definition"""
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()

    perks = models.ManyToManyField("experiences.perk")

    def __str__(self) -> str:
        return self.name
