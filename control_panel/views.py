from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth import logout
from django.contrib.auth.models import User
from control_panel.models import Book

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            if user.is_staff:
                
                login(request, user)
                return redirect('admin_dashboard')  
            else:
                
                messages.error(request, "You are not authorized to access the admin panel.")
                return render(request, 'control_panel/admin_login.html')  
        else:
            
            messages.error(request, "Invalid username or password.")
            return render(request, 'control_panel/admin_login.html')  

    return render(request, 'control_panel/admin_login.html')


def admin_dashboard(request):
    # Get the total number of users
    total_users = User.objects.count()
    
    # Get the total number of non-staff users
    non_staff_users = User.objects.filter(is_staff=False)
    
    # Get the total number of books
    total_books = Book.objects.count()

    # Get the number of active users (active users are those who have logged in recently)
    # Active users are those who have logged in within the last 30 days (you can adjust the filter)
    active_users = User.objects.filter(is_active=True)

    # Get recent activities for non-staff and staff users
    recent_non_staff_activities = non_staff_users.order_by('-last_login')[:5]  # Get the 5 most recent non-staff users' activities
    recent_admin_activities = User.objects.filter(is_staff=True).order_by('-last_login')[:5]  # Get the 5 most recent admin activities

    # Pass the data to the template
    context = {
        'total_users': total_users,
        'non_staff_users': non_staff_users.count(),
        'total_books': total_books,
        'active_users': active_users.count(),
        'recent_non_staff_activities': recent_non_staff_activities,
        'recent_admin_activities': recent_admin_activities,
    }

    return render(request, 'control_panel/admin_dashboard.html', context)

def admin_manage_users(request):
    # Your logic to handle the view for managing users
    return render(request, 'control_panel/manage_users.html')

def admin_manage_content(request):
    # Your logic for managing content
    return render(request, 'control_panel/manage_content.html')

def admin_settings(request):
    # Your logic for settings management
    return render(request, 'control_panel/settings.html')

def admin_logout(request):
    logout(request)
    return redirect('login')