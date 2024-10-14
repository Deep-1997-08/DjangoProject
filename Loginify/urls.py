from django.urls import path
from .views import print_hello

urlpatterns = [
    path('hello/',print_hello),
]