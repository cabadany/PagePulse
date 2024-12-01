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

def search_results(request):
    query = request.GET.get('q')
    results = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {'results': results, 'query': query})