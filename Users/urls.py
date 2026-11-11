from django.contrib import admin
from django.urls import path, include
from Users import views

urlpatterns = [
    path('', views.add_comment, name='add_comment'),
]