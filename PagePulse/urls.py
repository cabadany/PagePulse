"""
URL configuration for PagePulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('login_registration.urls')),
    path('forgot_password/', include('forgot_password.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('new_story/', include('book.urls')),
    path('my_stories/', include('book.urls')),
    path('mylibrary/', include('mylibrary.urls')),
    path('reading/', include('reading.urls')),
    path('profile/', include('profile_settings.urls')),
    path('control_panel/', include('control_panel.urls')),
    path('books/', include('book.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)