from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login_registration.models import Profile

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  

    return render(request, 'profile.html', {'profile': profile})