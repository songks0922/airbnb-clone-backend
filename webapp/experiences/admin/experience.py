from django.contrib import admin
from experiences.models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "price",
        "name",
        "start",
        "end",
        "created_at",
    )

    list_filter = (
        "category",
    )
