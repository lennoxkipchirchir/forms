from django.urls import path
from . import views

urlpartterns = [
    path('hello/', views.home, name='home'),
]