from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=50, choices=[
        ('Fiction', 'Fiction'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Adventure', 'Adventure'),
        ('LGBTQ+', 'LGBTQ+'),
        ('New Adult', 'New Adult'),
        ('Short Story', 'Short Story'),
    ])
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    target_audience = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    rating_mature = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.title}"

class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    current_chapter = models.ForeignKey('Chapter', on_delete=models.SET_NULL, null=True, blank=True)
    last_read_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
