from django.apps import AppConfig

class LoginRegistrationConfig(AppConfig):
    name = 'login_registration'

    def ready(self):
        import login_registration.signals