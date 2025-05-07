from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from book.models import Book, Chapter  # Import Book and Chapter models from the 'book' app
from mylibrary.models import UserLibrary  # Correct import path for UserLibrary model
from reading.models import ReadingProgress  # Import ReadingProgress model (if it's in the 'reading' app)
from django.contrib.auth.models import User  # Import the User model to check for the logged-in user

# This function will handle updating the user's reading progress
def update_progress(request):
    if request.method == 'POST':
        try:
            # Get the user library data from the request
            data = request.POST
            book_id = data.get('book_id')
            chapter_id = data.get('chapter_id')
            current_page = data.get('current_page', 0)

            # Get the user library instance (make sure user is authenticated)
            user_library = get_object_or_404(UserLibrary, user=request.user, book_id=book_id)
            chapter = get_object_or_404(Chapter, id=chapter_id)

            # Fetch the book using the book_id
            book = get_object_or_404(Book, id=book_id)

            # Update the current chapter and current page in the user's library
            user_library.current_chapter = chapter
            user_library.current_page = current_page

            # Update the reading progress
            total_pages = book.total_pages  # Make sure `total_pages` is available in the Book model
            user_library.update_progress(total_pages)

            # Save the changes to the UserLibrary
            user_library.save()

            return JsonResponse({'status': 'success', 'progress': user_library.progress})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


# This function handles displaying a book and its chapters
def read_book(request, book_id, chapter_id=None):
    # Fetch the book or return a 404 error if not found
    book = get_object_or_404(Book, id=book_id)
    
    # Get all chapters associated with this book, ordered by ID
    chapters = book.chapters.all().order_by('id')

    # If no chapter_id is provided, get the first chapter
    if chapter_id:
        # Ensure the chapter_id exists within the current book's chapters
        chapter = get_object_or_404(Chapter, id=chapter_id, book=book)
    else:
        # Default to the first chapter
        chapter = chapters.first()

    # If no chapters exist in the book, raise a 404 error
    if not chapters:
        raise Http404("This book has no chapters.")
    
    return render(request, 'readbook.html', {
        'book': book,
        'chapter': chapter,
        'chapters': chapters,
    })
    