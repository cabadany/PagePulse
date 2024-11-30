from django.db import models
from django.contrib.auth.models import User
from book.models import Book  # Assuming `Book` is in the `book` app

class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  # Prevents duplicate entries for the same book and user

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
