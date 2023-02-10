from django.urls import path
from categories.views import categories_view

urlpatterns = [
    path("", categories_view),
]