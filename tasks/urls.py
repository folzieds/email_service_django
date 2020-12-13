from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="task_home"),
    path("add", views.add_task, name="task_add")
]