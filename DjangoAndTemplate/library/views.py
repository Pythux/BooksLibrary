from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required # for function
from django.contrib.auth.mixins import LoginRequiredMixin # for class

from .models import Author, Subject, Book
from .forms import AuthorForm, SubjectForm, BookForm


class AuthorDetailView(DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm


class AuthorListView(ListView):
    model = Author


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ('description',)


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')


################################################
################### Subject ####################


class SubjectDetailView(DetailView):
    model = Subject


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm

class SubjectListView(ListView):
    model = Subject


class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    fields = ('name',)


class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('subject_list')


################################################
##################### BOOK #####################


class BookDetailView(DetailView):
    model = Book


def add_book_to_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.authors.add(author)
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(
        request, 'library/book_form.html',
        {'form': form, 'author': author})


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm

class BookListView(ListView):
    model = Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ('isbn', 'name', 'authors', 'subjects')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
