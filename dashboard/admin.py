from django.contrib import admin
from .models import Book, Chapter

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category', 'rating_mature')
    search_fields = ('title', 'author')
    list_filter = ('category', 'rating_mature')

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'published_date', 'book_image')  # Make sure 'book_image' is included here
        }),
        ('Details', {
            'fields': ('description', 'characters', 'category', 'target_audience', 'language', 'tags', 'rating_mature')
        }),
    )
    
    # To display the image as a thumbnail in the admin
    def book_image_thumbnail(self, obj):
        if obj.book_image:
            return '<img src="{}" width="100" height="100" />'.format(obj.book_image.url)
        return ''
    
    book_image_thumbnail.allow_tags = True  # This allows HTML rendering for the image

    # Add the image thumbnail to list display
    list_display = ('title', 'author', 'published_date', 'category', 'rating_mature', 'book_image_thumbnail')

admin.site.register(Book, BookAdmin)

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'created_at')  # Columns to display in the admin list view
    search_fields = ('title', 'book__title')  # Add search functionality
    list_filter = ('book',)  # Add filter options by book
    fields = ('book', 'title', 'content', 'created_at')  # Fields visible in the form
    readonly_fields = ('created_at',)  # Make 'created_at' non-editable

admin.site.register(Chapter,ChapterAdmin)