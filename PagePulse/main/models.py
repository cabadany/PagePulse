from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    # book_image = models.ImageField(upload_to='book_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    target_audience = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    rating_mature = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)