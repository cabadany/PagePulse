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
        title = request.POST.get('title')
        content = request.POST.get('content')

        Chapter.objects.create(book=book, title=title, content=content)

        return redirect('homepage')  

    return render(request, 'content_box.html', {'book': book})