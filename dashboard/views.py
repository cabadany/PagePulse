from django.shortcuts import render
from book.models import Book

def homepage(request):
    books = Book.objects.all()

    return render(request, 'homepage.html', {
        'books': books,
    })

def category_view(request, category):
    if category == 'All':
        books = Book.objects.all()
    else:
        books = Book.objects.filter(genre=category)
    
    return render(request, 'category_page.html', {'category': category, 'books': books})

def read_book(request, book_id, chapter_id=None):
    book = Book.objects.get(id=book_id)
    chapters = book.chapters.all().order_by('id')

    chapter = chapters.first() if not chapter_id else chapters.get(id=chapter_id)

    return render(request, 'readbook.html', {
        'book': book,
        'chapter': chapter,
        'chapters': chapters,
    })