from django.contrib import admin
from medias.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "experience",
    )

    list_filter = (
        "experience",
    )
