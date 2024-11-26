from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import BookForm
from .models import Book
import re  # Import regular expressions for password complexity check

def index(request):
    return render(request, 'main/index.html')

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
    
    return render(request, 'main/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')  # This field should be processed if added in the model
        username = request.POST.get('username')
        password = request.POST.get('password')
        terms = request.POST.get('terms')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
            return render(request, 'main/signup.html')

        # Check if terms and conditions are accepted
        if not terms:
            messages.error(request, "You must agree to the Terms and Conditions.")
            return render(request, 'main/signup.html')

        # Password complexity check
        if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messages.error(request, "Password must be at least 8 characters long, contain a letter, a number, and a special character.")
            return render(request, 'main/signup.html')

        # Create and save the user
        user = User.objects.create_user(
            username=username, 
            password=password, 
            first_name=first_name, 
            last_name=last_name
        )
        
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'main/signup.html')

def new_story(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New story created successfully!")
            return redirect('story_list')  # Ensure 'story_list' is defined in urls.py
    else:
        form = BookForm()
    return render(request, 'main/new_story.html', {'form': form})


def home(request):
    return HttpResponse("Welcome to the home page!")

def homepage(request):
    # Query all books to display in "For You" section
    books = Book.objects.all()

    # Query popular books for the "Popular" section (you may define what constitutes 'popular' based on rating or views)
    popular_books = Book.objects.filter(rating_mature=False)  # For example, filter out mature-rated books

    return render(request, 'main/homepage.html', {
        'books': books,
        'popular_books': popular_books,
    })

def forgot_password(request):
    return render(request, 'main/forgotpassword.html')

def digit_code(request):
    return render(request, 'main/digitcode.html')