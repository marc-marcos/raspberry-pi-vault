from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("repos", views.repos, name="repos"),
    path("passwords", views.passwords, name="passwords"),
]
