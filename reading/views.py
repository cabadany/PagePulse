from django.shortcuts import render
from book.models import Book

def read_book(request, book_id, chapter_id=None):
    book = Book.objects.get(id=book_id)
    chapters = book.chapters.all().order_by('id')

    chapter = chapters.first() if not chapter_id else chapters.get(id=chapter_id)

    return render(request, 'readbook.html', {
        'book': book,
        'chapter': chapter,
        'chapters': chapters,
    })