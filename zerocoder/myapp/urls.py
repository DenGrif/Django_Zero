from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data_view, name='data-view'),   # Имя маршрута: data-view
    path('test/', views.test_view, name='test-view'),   # Имя маршрута: test-view
]
