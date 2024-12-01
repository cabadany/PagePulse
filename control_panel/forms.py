from django import forms
from django.contrib.auth.models import User
from .models import Content, Book
from .models import Settings


# UserForm for user registration and management
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff', 'is_superuser']
    
    # Overriding save method to hash password
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password'])  # Hash the password
            user.save()
        return user

# ContentForm for managing content-related data
class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'author', 'published_date', 'genre', 'book_image']

# BookForm for managing book-related data
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'book_image']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['site_name', 'site_logo', 'admin_email', 'contact_info', 'theme']