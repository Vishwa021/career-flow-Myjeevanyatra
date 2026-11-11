from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test_view, name='test'),
    path('submit/', views.submit_test, name='submit_test'),
    path('result/', views.result, name='result'),
]