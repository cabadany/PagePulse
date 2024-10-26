from django.urls import path
from .views import index, login_view, signup_view  # Ensure signup_view is imported

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),  # This line defines the signup route
]