from django.urls import path
from . import views

urlpatterns = [
    path('', views.forgot_password_view, name='forgot_password'),
]