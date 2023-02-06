from django.contrib import admin
from medias.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "room",
        "experience",
    )

    list_filter = (
        "room",
        "experience",
    )
