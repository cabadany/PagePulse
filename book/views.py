from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Chapter, Book

def my_stories(request):
    return render(request, 'my_stories.html')

def new_chapter(request):
    return render(request, 'new_chapter.html')

def new_story(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('content_box', book_id=book.id)
    else:
        form = BookForm()

    return render(request, 'new_story.html', {'form': form})

def content_box(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        # Get the data from the form
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Debugging: Check if data is being passed
        print(f"Received title: {title}")
        print(f"Received content: {content}")

        if title and content:
            # Save the new chapter to the database
            new_chapter = Chapter(book=book, title=title, content=content)
            new_chapter.save()

            # Debugging: Print saved chapter to ensure it's stored
            print(f"Saved chapter: {new_chapter}")

            # Redirect to the same page to clear the form (and avoid resubmission issues)
            return redirect('content_box', book_id=book.id)
        else:
            # If title or content are missing, show an error message
            error_message = "Both title and content are required."
            return render(request, 'content_box.html', {'book': book, 'error_message': error_message})

    return render(request, 'content_box.html', {'book': book})