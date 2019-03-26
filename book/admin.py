from django.contrib import admin
from .models import Book




class BookAdmin(admin.ModelAdmin):
    list_display = ["book_name","date"]
    list_filter = ["date"]

admin.site.register(Book,BookAdmin)

