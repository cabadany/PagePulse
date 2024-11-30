from django.contrib import admin
from .models import UserLibrary

@admin.register(UserLibrary)
class UserLibraryAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    search_fields = ('user__username', 'book__title')
    list_filter = ('added_date',)
