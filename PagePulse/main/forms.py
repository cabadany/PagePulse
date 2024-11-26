from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
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