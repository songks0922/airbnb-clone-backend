from django.contrib import admin
from experiences.models import Perk


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "details",
        "explanation"
    )
