from django.shortcuts import render
from .models import Book, ReadingProgress

def homepage(request):
    # Query all books to display in "For You" section
    books = Book.objects.all()

    # Query popular books for the "Popular" section (you may define what constitutes 'popular' based on rating or views)
    popular_books = Book.objects.filter(rating_mature=False)  # For example, filter out mature-rated books

    return render(request, 'homepage.html', {
        'books': books,
        'popular_books': popular_books,
    })

def read_book(request, book_id, chapter_id=None):
    book = Book.objects.get(id=book_id)
    chapters = book.chapters.all().order_by('id')

    # Get the requested chapter or default to the first chapter
    chapter = chapters.first() if not chapter_id else chapters.get(id=chapter_id)

    # Update or create reading progress
    progress, created = ReadingProgress.objects.get_or_create(user=request.user, book=book)
    progress.current_chapter = chapter
    progress.save()

    return render(request, 'readbook.html', {
        'book': book,
        'chapter': chapter,
        'chapters': chapters,
        'progress': progress
    })