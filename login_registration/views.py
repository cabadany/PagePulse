from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
import re

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
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        username = request.POST.get('username')
        password = request.POST.get('password')
        terms = request.POST.get('terms')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return render(request, 'main/signup.html')

        if not terms:
            messages.error(request, "You must agree to the Terms and Conditions.")
            return render(request, 'main/signup.html')

        if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.error(request, "Password must be at least 8 characters long, contain a letter, a number, and a special character.")
            return render(request, 'signup.html')

        user = User.objects.create_user(
            username=username, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )
        
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'signup.html')