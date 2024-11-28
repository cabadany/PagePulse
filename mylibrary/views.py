from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserLibrary
from book.models import Book

@login_required
def user_library(request):
    user_library_books = UserLibrary.objects.filter(user=request.user)
    return render(request, 'userlibrary/library.html', {'user_library_books': user_library_books})

@login_required
def add_to_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    UserLibrary.objects.get_or_create(user=request.user, book=book)
    return redirect('user_library')

@login_required
def update_progress(request, library_id, progress):
    user_library_entry = get_object_or_404(UserLibrary, id=library_id, user=request.user)
    user_library_entry.progress = progress
    user_library_entry.is_completed = progress == 100
    user_library_entry.save()
    return redirect('user_library')
