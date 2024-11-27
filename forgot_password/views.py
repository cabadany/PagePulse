from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
import random

# Store temporary data (should ideally use sessions or database)
codes = {}

def forgot_password_view(request):
    #if request.method == 'POST':
        #email = request.POST.get('email')
        #code = str(random.randint(1000, 9999))  # Generate a 4-digit code
        #codes[email] = code  # Save code temporarily (can be stored in DB instead)

        # Send the 4-digit code to the user's email
        #send_mail(
            #'Your Password Reset Code',
            #f'Your verification code is {code}',
            #'noreply@pagepulse.com',
            #[email],
            #fail_silently=False,
        #)
        #return redirect(reverse('digitcode'))  # Redirect to digitcode page
    return render(request, 'forgotpassword.html')

def digitcode_view(request):
    #if request.method == 'POST':
        #email = request.POST.get('email')
        #entered_code = request.POST.get('code')

        # Verify the code
        #if email in codes and codes[email] == entered_code:
            #del codes[email]  # Remove code after verification
            #return redirect(reverse('changepassword'))  # Redirect to changepassword
        #else:
            #return render(request, 'digitcode.html', {'error': 'Invalid code. Please try again.'})
    return render(request, 'digitcode.html')

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def change_password(request):
    #if request.method == 'POST':
        #email = request.POST.get('email')
        #new_password = request.POST.get('password')

        # Assuming you're using Django's default User model
        #user = User.objects.get(email=email)
        #user.password = make_password(new_password)  # Hash the new password
        #user.save()

        #return redirect('login')  # Redirect to login after password reset
    return render(request, 'changepassword.html')


