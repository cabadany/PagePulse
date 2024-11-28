from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_library, name='user_library'),
    path('add/<int:book_id>/', views.add_to_library, name='add_to_library'),
    path('update-progress/<int:library_id>/<int:progress>/', views.update_progress, name='update_progress'),
]
