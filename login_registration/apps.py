# login_registration/apps.py

from django.apps import AppConfig

class LoginRegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_registration'  # Ensure this matches the app name in INSTALLED_APPS

    def ready(self):
        import login_registration.signals  # Correct import path
