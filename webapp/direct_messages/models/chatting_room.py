from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """ Room Model Definition """

    class Meta:
        db_table = 'chatting_room'
        verbose_name = 'ChattingRoom'
        verbose_name_plural = 'ChattingRooms'

    users = models.ManyToManyField("users.User")

    def __str__(self) -> str:
        return "Chatting Room."
