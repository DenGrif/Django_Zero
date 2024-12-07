from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Главная страница main
    path('new', views.new)
]
