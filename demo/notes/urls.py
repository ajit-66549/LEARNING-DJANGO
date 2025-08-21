from django.urls import path
from . import views

urlpatterns = [
    path("view/", views.mynote, name="note"),
    path("add/", views.adding_note, name="add_note")
]
