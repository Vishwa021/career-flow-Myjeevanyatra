"""
URL configuration for new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content_manager.urls')),
    path('blog/<str:slug>', views.blog, name='blog'),
    path('add_comment/<str:slug>',views.add_comment, name='add_comment'),
    path('career/<str:slug_urls>', include('Career.urls')),
    path('test/', include(('Questions.urls', 'questions'), namespace='questions')),
    path('write_blog/', views.write_blog, name='write_blog'),
]
