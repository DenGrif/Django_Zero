from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    # path('test/', views.test_view, name='test-view'),   # Имя маршрута: test-view
]
