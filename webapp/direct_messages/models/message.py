from django.db import models
from common.models import CommonModel


class Message(CommonModel):
    """ Message Model Definition """

    class Meta:
        db_table = 'message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
