from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category', 'rating_mature')
    search_fields = ('title', 'author')
    list_filter = ('category', 'rating_mature')

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'published_date', 'book_image')
        }),
        ('Details', {
            'fields': ('description', 'characters', 'category', 'target_audience', 'language', 'tags', 'rating_mature')
        }),
    )

admin.site.register(Book, BookAdmin)