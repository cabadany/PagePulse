from django.shortcuts import render
from .models import Book
                    
def homepage(request):
    books = Book.objects.all()
    return render(request, 'homepage.html', {'books': books})