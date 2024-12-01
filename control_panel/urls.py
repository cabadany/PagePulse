from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('manage-users/', views.admin_manage_users, name='admin_manage_users'),
    path('add-user/', views.admin_add_user, name='admin_add_user'),
    path('edit/<int:user_id>/', views.edit_user, name='admin_edit_user'),
    path('suspend/<int:user_id>/', views.suspend_user, name='admin_suspend_user'),
    path('delete/<int:user_id>/', views.delete_user, name='admin_delete_user'),

    path('manage-content/', views.admin_manage_content, name='admin_manage_content'),

    path('settings/', views.admin_settings, name='admin_settings'),
    
    path('logout/', views.admin_logout, name='admin_logout'),
]
