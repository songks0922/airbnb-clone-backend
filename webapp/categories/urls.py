from django.urls import path
from categories.views import Categories
from categories.views import CategoryDetail
from categories.views import CategoryViewSet

urlpatterns = [
    path("", CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("<int:pk>", CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy'
    })),
]
