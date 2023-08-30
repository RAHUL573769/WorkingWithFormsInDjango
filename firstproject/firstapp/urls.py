from django.urls import path

from . import views

urlpatterns = [
    path("template", views.home, name="homepage"),
    path("", views.about, name="about"),
    path("dynamic/<slug:courseid>", views.dynamic),
]
