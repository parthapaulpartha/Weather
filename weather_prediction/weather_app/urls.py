"""weather_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.contrib import admin
# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),

    # Weather prediction Starts from here
    path(r'weather_predict/', views.weather_prediction, name='weather_predict'),
    path(r'weather_predict/result/', views.weather_result, ),
    # Weather prediction End here 

    # About us start
    path(r'about/', views.about, name='about')
]
