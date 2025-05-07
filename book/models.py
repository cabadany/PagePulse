from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    book_image = models.ImageField(upload_to='books/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total_pages = models.IntegerField(default=0)
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

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.title}"


class Comment(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chapter = models.ForeignKey('Chapter', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.created_at}"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE)
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"Bookmark for {self.user} in {self.book} at position {self.position}"


class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    current_page = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - Page {self.current_page}"

    @property
    def progress_percentage(self):
        if self.book.total_pages > 0:
            return (self.current_page / self.book.total_pages) * 100
        return 0  # Return 0% if the book has no pages defined
