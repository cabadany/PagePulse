from django.shortcuts import render

def my_stories(request):
    return render(request, 'my_stories.html')

def new_story(request):
    return render(request, 'new_story.html')