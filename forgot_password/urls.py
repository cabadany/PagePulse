from django.urls import path
from . import views

urlpatterns = [
    path('', views.forgot_password_view, name='forgotpassword'),  
    path('digitcode/', views.digitcode_view, name='digitcode'),   
    path('changepassword/', views.change_password, name='changepassword'),

]

