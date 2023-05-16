from django.urls import path
from recipes.views import home

# HTTP REQUEST


urlpatterns = [
    path("", home),  # Home
]
