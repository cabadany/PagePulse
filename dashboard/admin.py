from django.contrib import admin
# from .models import Book, Chapter

# The BookAdmin and ChapterAdmin classes are commented out to avoid errors since Book is no longer used

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date', 'genre', 'book_image_thumbnail')  # Use genre instead of category
#     search_fields = ('title', 'author')
#     list_filter = ('genre',)

#     fieldsets = (
#         (None, {
#             'fields': ('title', 'author', 'published_date', 'cover_image')
#         }),
#         ('Details', {
#             'fields': ('description', 'genre')
#         }),
#     )

#     def book_image_thumbnail(self, obj):
#         if obj.cover_image:
#             return '<img src="{}" width="100" height="100" />'.format(obj.cover_image.url)
#         return ''

# book_image_thumbnail.allow_tags = True

# admin.site.register(Book, BookAdmin)

# class ChapterAdmin(admin.ModelAdmin):
#     list_display = ('title', 'book', 'created_at')
#     search_fields = ('title', 'book__title')
#     list_filter = ('book',) 
#     fields = ('book', 'title', 'content', 'created_at') 
#     readonly_fields = ('created_at',)

# admin.site.register(Chapter, ChapterAdmin)