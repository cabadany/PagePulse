from . import views
from django.urls import path
from .views import index, login_view, signup_view, new_story
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('new_story/', new_story, name='new_story'),
    path('home/', views.homepage, name='homepage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)