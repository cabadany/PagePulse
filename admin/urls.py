# myproject/urls.py
from django.urls import path
from admin.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
]