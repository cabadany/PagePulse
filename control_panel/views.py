from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth import logout

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
    return render(request, 'control_panel/admin_dashboard.html')

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