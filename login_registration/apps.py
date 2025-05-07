# login_registration/apps.py
from django.apps import AppConfig

class LoginRegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_registration'

    def ready(self):
        import login_registration.signals  # This is where you import the signals to ensure they are connected
