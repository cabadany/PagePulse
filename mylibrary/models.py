from django.db import models
from django.contrib.auth.models import User
from book.models import Book, Chapter

class UserLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
    current_page = models.PositiveIntegerField(default=0)
    current_chapter = models.ForeignKey(Chapter, null=True, blank=True, on_delete=models.SET_NULL)  # This is the missing field
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def update_progress(self, total_pages):
        if total_pages > 0:
            self.progress = int((self.current_page / total_pages) * 100)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
