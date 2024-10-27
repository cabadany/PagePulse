from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            dob = form.cleaned_data.get('dob')  # Store or use as needed

            # Create a new user
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
               

                messages.success(request, 'Your account has been created! You can now log in.')
                return redirect(reverse('login'))  # Redirect to login or another page
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()  # Instantiate the form for GET request

    return render(request, 'signup.html', {'form': form})
