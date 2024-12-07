from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', include('main.urls')),  # Главные маршруты для приложения main
    # path('myapp/', include('myapp.urls')),  # Маршруты для приложения myapp
]


# urlpatterns = [
#     path('admin/', admin.site.urls),  # Админка
#     path('', include('main.urls')),  # Главные маршруты для приложения main
#     path('myapp/', include('myapp.urls')),  # Маршруты для приложения myapp
# ]
