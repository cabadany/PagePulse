from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'password_reset_email.html'  # Custom email template
    subject_template_name = 'password_reset_subject.txt'  # Optional custom subject template
    
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, **kwargs):
        # Render subject and email content
        subject = render_to_string(subject_template_name, context).strip()
        message = render_to_string(email_template_name, context)

        # Send the email
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            **kwargs
        )
