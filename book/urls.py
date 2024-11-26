from django.urls import path
from . import views

urlpatterns = [
    path('new_story/', views.new_story, name='new_story'),
    path('my_stories/', views.my_stories, name='my_stories'),
]