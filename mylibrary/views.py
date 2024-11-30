from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserLibrary
from book.models import Book
from django.http import JsonResponse

@login_required
def user_library(request):
    user_library_books = UserLibrary.objects.filter(user=request.user)
    return render(request, 'private_library.html', {'user_library_books': user_library_books})

@login_required
def add_to_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Check if the book is already in the user's library
    if not UserLibrary.objects.filter(user=request.user, book=book).exists():
        # Add the book to the user's library
        UserLibrary.objects.create(user=request.user, book=book)
        message = "Book added to your library."
    else:
        message = "This book is already in your library."

    # Return a JSON response to notify the front-end
    return JsonResponse({'message': message})