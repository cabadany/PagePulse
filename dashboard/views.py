from django.shortcuts import render
from book.models import Book

def homepage(request):
    books = Book.objects.all()

    return render(request, 'homepage.html', {
        'books': books,
    })

def read_book(request, book_id, chapter_id=None):
    book = Book.objects.get(id=book_id)
    chapters = book.chapters.all().order_by('id')

    chapter = chapters.first() if not chapter_id else chapters.get(id=chapter_id)

    progress, created = ReadingProgress.objects.get_or_create(user=request.user, book=book)
    progress.current_chapter = chapter
    progress.save()

    return render(request, 'readbook.html', {
        'book': book,
        'chapter': chapter,
        'chapters': chapters,
        'progress': progress
    })