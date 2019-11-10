from django.urls import path
from GridDemoApp import views

urlpatterns = [
    path("", views.home, name="home"),
]
