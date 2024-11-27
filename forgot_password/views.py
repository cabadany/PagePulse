from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse
import random
from django.core.cache import cache  # Import cache to temporarily store the verification code
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Forgot Password view: User enters email
def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if email exists in the database
        if User.objects.filter(email=email).exists():
            # Generate a 4-digit verification code
            code = str(random.randint(1000, 9999))
            # Store the code in the cache for 10 minutes
            cache.set(email, code, timeout=600)  # Timeout set to 10 minutes

            # Send the 4-digit code to the user's email
            send_mail(
                'Your Password Reset Code',
                f'Your verification code is {code}',
                'pagepulse.pulse@gmail.com',  # Sender email
                [email],
                fail_silently=False,
            )

            # Redirect to digitcode view for entering the verification code
            return redirect(reverse('digitcode'))  # Ensure it redirects to 'digitcode' page after sending the code
        else:
            # If the email is not found, add an error message
            messages.error(request, "We couldn't find an account associated with this email address.")
            return render(request, 'forgotpassword.html')  # Stay on the forgot password page with error message

    return render(request, 'forgotpassword.html')


# Digit Code view: User enters the code received in the email
def digitcode_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        entered_code = request.POST.get('code')

        # Retrieve the verification code from the cache
        cached_code = cache.get(email)

        # Check if the code exists in cache
        if cached_code:
            # Verify the entered code matches the cached code
            if cached_code == entered_code:
                cache.delete(email)  # Clear the code after successful verification
                return redirect(reverse('changepassword'))  # Redirect to password change page
            else:
                messages.error(request, "Invalid code. Please try again.")
                return render(request, 'digitcode.html')
        else:
            # If code is not found in cache (may expire), show an error message
            messages.error(request, "Verification code has expired or is invalid.")
            return redirect(reverse('forgotpassword'))  # Go back to forgot password page

    return render(request, 'digitcode.html')


# Change Password view: User can change their password after successful code verification
def change_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('password')

        # Find the user by email and update the password
        try:
            user = User.objects.get(email=email)
            user.password = make_password(new_password)  # Hash the new password
            user.save()

            messages.success(request, "Your password has been successfully updated.")
            return redirect('login')  # Redirect to login page after successful password change
        except User.DoesNotExist:
            messages.error(request, "Error: User not found.")
            return redirect('forgot_password')  # Redirect to the forgot password page if user not found

    return render(request, 'changepassword.html')
