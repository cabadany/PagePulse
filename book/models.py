from django.db import models

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

    def __str__(self):
        return self.title
    
   
class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.title}"