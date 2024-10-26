from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Make sure to include the namespace if you're using it
    path('login/', views.login_view, name='login'),
]