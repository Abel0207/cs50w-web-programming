from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.great, name="great"),
    path("abel", views.abel, name="abel"),
    path("kelly", views.kelly, name="kelly"),
]