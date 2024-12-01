from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
import re
from .models import Profile

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password').strip()
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST.get('username').strip()
        terms = request.POST.get('terms')

        if len(username) < 4:
            messages.error(request, "Username must be at least 4 characters long.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please choose another one.")
            return render(request, 'signup.html')

        if not terms:
            messages.error(request, "You must agree to the Terms and Conditions.")
            return render(request, 'signup.html')

        if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password) or not re.search(r"[^\w\s]", password):
            messages.error(request, "Password must be at least 8 characters long, contain a letter, a number, and a special character.")
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(
                username=username, 
                password=password, 
                first_name=first_name, 
                last_name=last_name,
                email=email,
            )

            if profile_picture:
                user.profile.profile_picture = profile_picture
                user.profile.save()

            user.save()
            messages.success(request, "Account created successfully! Redirecting to login page...")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')