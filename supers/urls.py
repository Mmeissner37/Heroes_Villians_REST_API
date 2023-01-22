from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.super_list), 
    path('<int:pk>', views.super_detail)
]

