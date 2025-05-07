from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Chapter, Book, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Bookmark
import json
import logging

@login_required
def my_stories(request):
    user_books = Book.objects.filter(author=request.user)

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
        form = BookForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('story_success')  
        else:
            print(form.errors)  
    else:
        form = BookForm()
    
    return render(request, 'story_create.html', {'form': form})

def chapter_detail(request, book_id, chapter_id):
    book = get_object_or_404(Book, id=book_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, book=book)

    if request.method == 'POST':
        user = request.POST.get('user')  
        content = request.POST.get('content')  

        if user and content:
            Comment.objects.create(
                user=user,
                content=content,
                chapter=chapter
            )
            return redirect('chapter_detail', book_id=book.id, chapter_id=chapter.id)

    comments = chapter.comments.all()

    return render(request, 'chapter_detail.html', {
        'book': book,
        'chapter': chapter,
        'comments': comments,
    })

@csrf_exempt  
def save_bookmark(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) 
            book_id = data.get('book_id')
            position = data.get('position')

            bookmark = Bookmark.objects.create(book_id=book_id, position=position, user=request.user)
            bookmark.save()

            return JsonResponse({"status": "success"})  
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})  
    return JsonResponse({"status": "error", "message": "Invalid request method"})

def chapter_view(request, book_id, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id, book_id=book_id)
    
    saved_position = Bookmark.objects.filter(user=request.user, book_id=book_id).first()
    saved_position = saved_position.position if saved_position else 0
    
    return render(request, 'chapter.html', {
        'chapter': chapter,
        'saved_position': saved_position,
        'book': chapter.book
    })

def update_progress(request, book_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        current_page = data.get('current_page')
        
        # Get the bookmark for the user and the specific book
        bookmark = get_object_or_404(Bookmark, user=request.user, book_id=book_id)
        
        # Update the position of the bookmark
        bookmark.position = current_page
        bookmark.save()

        # Calculate the progress percentage
        total_pages = bookmark.book.total_pages
        progress_percentage = (current_page / total_pages) * 100

        # Return the updated progress percentage
        return JsonResponse({'progress': progress_percentage})