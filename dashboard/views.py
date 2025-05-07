from django.shortcuts import render
from book.models import Book
from django.contrib.auth.models import User

def homepage(request):
    books = Book.objects.all()
    user = request.user if request.user.is_authenticated else None
    
    # Recommendation logic based on genre preferences
    recommended_books = []
    if user and user.profile.favorite_genre:
        # Get the first 5 books (to avoid recommending the same books)
        exclude_books = books[:5].values_list('id', flat=True)
        
        # Filter recommended books based on the user's favorite genre and exclude books already shown
        recommended_books = Book.objects.filter(genre=user.profile.favorite_genre).exclude(id__in=exclude_books)

    return render(request, 'homepage.html', {
        'books': books,
        'user': user,
        'recommended_books': recommended_books,
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
