from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("irina", views.irina, name="irina"),
    path("danil", views.danil, name="danil")
]