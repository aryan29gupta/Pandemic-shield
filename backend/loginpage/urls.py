from django.contrib import admin
from django.urls import path
from loginpage import views

urlpatterns = [
    path('', views.index,name="loginpage"),
]
