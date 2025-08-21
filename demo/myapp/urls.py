from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("temp/", views.temp, name="temp"),
    path("todos/", views.todos, name="todos")
]
