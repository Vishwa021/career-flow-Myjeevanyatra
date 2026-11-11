from django.contrib import admin
from django.urls import path
from content_manager import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="registeration"),
    path("login", views.login_views , name="login"),
    path("logout", views.logout_user, name="logout"),
        
]