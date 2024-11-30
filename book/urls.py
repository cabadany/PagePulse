from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('my-stories/', views.my_stories, name='my_stories'),
    path('new-story/', views.new_story, name='new_story'),
    path('new-chapter/', views.content_box, name='content_box'),
    path('my-stories/content-box/<int:book_id>/', views.content_box, name='content_box'),
    path('my-stories/content-box/<int:book_id>/', views.content_box, name='new_chapter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)