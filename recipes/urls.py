from django.urls import path

from . import views

# HTTP REQUEST


urlpatterns = [
    path("", views.home, name="recipes-home"),
    path("recipes/<int:id>/", views.recipe, name="recipes-recipe"),
    ]  # Home
