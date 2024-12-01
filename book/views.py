from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Chapter, Book
from django.contrib.auth.decorators import login_required

@login_required
def my_stories(request):
    # Adjust the field name to 'author' or the appropriate field in your model
    user_books = Book.objects.filter(author=request.user)

    # Pass the user_books to the template
    return render(request, 'my_stories.html', {'user_books': user_books})

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
        title = request.POST.get('title')
        content = request.POST.get('content')

        print(f"Received title: {title}")
        print(f"Received content: {content}")

        if title and content:
            new_chapter = Chapter(book=book, title=title, content=content)
            new_chapter.save()

            print(f"Saved chapter: {new_chapter}")

            return redirect('content_box', book_id=book.id)
        else:
            error_message = "Both title and content are required."
            return render(request, 'content_box.html', {'book': book, 'error_message': error_message})

    return render(request, 'content_box.html', {'book': book})

def story_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('story_success')  # Redirect after saving
        else:
            print(form.errors)  # Debug: Check for any form errors
    else:
        form = BookForm()
    
    return render(request, 'story_create.html', {'form': form})