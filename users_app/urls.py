from django.urls import path
from users_app import views
from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name = 'logout'),
]