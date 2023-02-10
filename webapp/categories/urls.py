from django.urls import path
from categories.views import categories_view
from categories.views import category_view


urlpatterns = [
    path("", categories_view),
    path("<int:pk>", category_view),
]