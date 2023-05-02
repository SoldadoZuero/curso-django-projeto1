from django.urls import path
from recipes.views import home, contact, about

# HTTP REQUEST


urlpatterns = [
    path('', home),  # Home
    path('about/', about),  # /sobre/
    path('contact/', contact),  # /contato/
]
