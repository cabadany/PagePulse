from django.shortcuts import render

def forgot_password_view(request):
    return render(request, 'forgotpassword.html')

def digitcode_view(request):
    # Your view logic here
    return render(request, 'digitcode.html')

def reset_password_view(request):
    # Your logic for resetting password
    return render(request, 'resetpassword.html')