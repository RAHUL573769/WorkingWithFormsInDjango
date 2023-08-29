from django.urls import path

from . import views

urlpatterns = [
    path("template", views.home),
    path("", views.about),
    path("dynamic/<slug:courseid>", views.dynamic),
]
