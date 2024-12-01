from django import forms
from .models import Book, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'book_image', 'description', 'genre']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content']

    user = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add your comment here...'}))