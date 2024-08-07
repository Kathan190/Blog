from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
   path('', views.index, name="index"),
   path('about', views.about, name="about"),
   path('blogpost/<int:id>', views.blogpost, name="blogpost"),
]