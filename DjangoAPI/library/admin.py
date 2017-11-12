from django.contrib import admin

from .models import Author, Subject, Book

admin.site.register(Author)
admin.site.register(Subject)
admin.site.register(Book)
