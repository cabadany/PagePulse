from django.contrib import admin
from django.contrib.auth.models import User  # Import the default User model
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'created_at')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

# Optional: Register the User model if you want to customize its display in the admin panel
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')

admin.site.unregister(User)  # Unregister the default User model to re-register it with custom admin
admin.site.register(User, UserAdmin)  # Re-register User with custom admin
