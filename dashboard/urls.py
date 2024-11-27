from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('read/<int:book_id>/', views.read_book, name='read_book'),
    path('read/<int:book_id>/<int:chapter_id>/', views.read_book, name='read_specific_chapter'),
    path('category/<str:category>/', views.category_view, name='category_view'),
]