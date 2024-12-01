from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserLibrary
from book.models import Book, Chapter
from django.http import JsonResponse
from django.core.paginator import Paginator
import json

@login_required
def user_library(request):
    user_library_books = UserLibrary.objects.filter(user=request.user)
    return render(request, 'private_library.html', {'user_library_books': user_library_books})

@login_required
def add_to_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if not UserLibrary.objects.filter(user=request.user, book=book).exists():
        UserLibrary.objects.create(user=request.user, book=book)
        message = "Book added to your library."
    else:
        message = "This book is already in your library."

    return JsonResponse({'message': message})

def remove_from_library(request, user_library_id):
    user_library = UserLibrary.objects.get(id=user_library_id)
    user_library.delete() 
    return redirect('user_library') 

@login_required
def update_bookmark(request, book_id):
    if request.method == 'POST':
        user_library = get_object_or_404(UserLibrary, user=request.user, book_id=book_id)

        try:
            current_chapter_id = int(request.POST.get('current_chapter_id', 0))
            current_page = int(request.POST.get('current_page', 0))
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid input'})

        current_chapter = get_object_or_404(Chapter, id=current_chapter_id)
        user_library.current_chapter = current_chapter
        user_library.current_page_in_chapter = current_page
        user_library.update_progress()
        user_library.save()

        return JsonResponse({'status': 'success', 'progress': user_library.progress})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def read_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        return render(request, 'readbook.html', {'book': book})
    except Book.DoesNotExist:
        return render(request, '404.html') 