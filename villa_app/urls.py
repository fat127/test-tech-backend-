from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URLs
    path('api/', include('main.urls')),  # Include main app's URLs for API-related endpoints
    path('auth/', include('main.urls')),  # Include main app's URLs for auth-related endpoints
]
