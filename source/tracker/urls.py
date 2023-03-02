from django.urls import path

from .views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
]