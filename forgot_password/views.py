from django.shortcuts import render

def forgot_password_view(request):
    return render(request, 'forgotpassword.html')
