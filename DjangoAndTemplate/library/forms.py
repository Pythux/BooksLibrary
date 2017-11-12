from django import forms
from .models import Author, Subject, Book


class AuthorForm(forms.ModelForm):

    class Meta():
        model = Author
        fields = ('first_name', 'last_name', 'description')


class BookForm(forms.ModelForm):

    class Meta():
        model = Book
        fields = ('isbn', 'name', 'authors', 'subjects')


class SubjectForm(forms.ModelForm):

    class Meta():
        model = Subject
        fields = ('name',)
