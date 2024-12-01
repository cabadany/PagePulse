from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action} - {self.timestamp}'
    
class Content(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Settings(models.Model):
    site_name = models.CharField(max_length=100)
    site_logo = models.ImageField(upload_to='logos/')
    admin_email = models.EmailField()
    contact_info = models.TextField()
    theme = models.CharField(max_length=20, choices=[('light', 'Light'), ('dark', 'Dark')])
    
    def __str__(self):
        return self.site_name