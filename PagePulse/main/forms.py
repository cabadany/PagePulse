# main/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'description', 'characters', 'category', 'target_audience',
            'language', 'tags', 'rating_mature'
        ]
        widgets = {
            'rating_mature': forms.CheckboxInput(),
        }