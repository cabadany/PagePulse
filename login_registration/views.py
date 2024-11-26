from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the PagePulse homepage!")

def signup_view(request):
    return HttpResponse("Signup page")

def login_view(request):
    return HttpResponse("Login page")