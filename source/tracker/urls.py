from django.urls import path

from .views.base import index_view
from .views.tasks import add_view

urlpatterns = [
    path("", index_view, name='index'),
    path("task/add/", add_view, name='task_add')
]