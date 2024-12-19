from django.urls import path
from .views import login_view, logout_view, get_user, villa_list, villa_detail

urlpatterns = [
    path('login/', login_view, name='login'),  # Login endpoint
    path('logout/', logout_view, name='logout'),  # Logout endpoint
    path('user/', get_user, name='get_user'),  # Get user info endpoint
    path('villa/', villa_list, name="villa_list"),  # Villa list endpoint
    path('villa/<int:id>/', villa_detail, name="villa_detail"),  # Villa detail endpoint
]
