from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseForbidden

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

