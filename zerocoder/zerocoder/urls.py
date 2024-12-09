from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', include('main.urls')),  # Главные маршруты для приложения main
    path('news/', include('myapp.urls')),  # Маршруты для приложения myapp
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
#     path('admin/', admin.site.urls),  # Админка
#     path('', include('main.urls')),  # Главные маршруты для приложения main
#     path('myapp/', include('myapp.urls')),  # Маршруты для приложения myapp
# ]
