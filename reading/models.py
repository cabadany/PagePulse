from django.db import models
from django.contrib.auth.models import User
from book.models import Book  # Assuming Book is defined in the book app

class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_progresses')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_progresses')
    current_page = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - Page {self.current_page}"

    @property
    def progress_percentage(self):
        if self.book.total_pages > 0:
            return (self.current_page / self.book.total_pages) * 100
        return 0  # Avoid division by zero if total_pages is 0
