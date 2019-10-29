from django.urls import path
from inlineForm import views

urlpatterns = [
    path("", views.home, name="home"),
]
