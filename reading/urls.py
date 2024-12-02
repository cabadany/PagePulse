from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('read/<int:book_id>/', views.read_book, name='read_book'),
    path('read/<int:book_id>/<int:chapter_id>/', views.read_book, name='read_specific_chapter'),
    path('update_progress/', views.update_progress, name='update_progress'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)