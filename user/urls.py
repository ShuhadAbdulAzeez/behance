from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="register"),
]
