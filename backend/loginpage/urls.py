from django.contrib import admin
from django.urls import path
from loginpage import views

urlpatterns = [
    path('', views.index,name="loginpage"),
    path('home/', views.home,name="home"),
    path('symptoms/', views.index,name="symptoms"),
    path('checkarea/', views.index,name="checkarea"),
    path('safeport/', views.index,name="safeport"),
]
