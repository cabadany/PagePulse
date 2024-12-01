from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-users/', views.admin_manage_users, name='admin_manage_users'),
    path('manage-content/', views.admin_manage_content, name='admin_manage_content'),
    path('settings/', views.admin_settings, name='admin_settings'),
    path('logout/', views.admin_logout, name='admin_logout'),
]
