from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.index, name='index'),
    path('terms/', views.terms_conditions, name='terms_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)