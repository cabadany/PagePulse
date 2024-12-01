from django.urls import path
from . import views

urlpatterns = [
    path('user-library/', views.user_library, name='user_library'),
    path('add-to-library/<int:book_id>/', views.add_to_library, name='add_to_library'),
    path('remove_from_library/<int:user_library_id>/', views.remove_from_library, name='remove_from_library'),
]
