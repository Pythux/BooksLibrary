from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=80, db_index=True)
    last_name = models.CharField(max_length=80, db_index=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('first_name',)


class Subject(models.Model):
    name = models.CharField(max_length=80, primary_key=True)

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name).capitalize()


ISBN_VALIDATOR = RegexValidator(
    # regex=r'^(ISBN[-]*(1[03])*[ ]*(: ){0,1})*' ...
    regex=r'(([0-9Xx][- ]*){13}|([0-9Xx][- ]*){10})$',
    message='Should be an ISBN',
    code='nomatch')


class Book(models.Model):
    isbn = models.CharField(
        max_length=28, primary_key=True, validators=[ISBN_VALIDATOR])
    name = models.CharField(max_length=200)
    # django related_name: author.book_set
    authors = models.ManyToManyField(Author, related_name='books', blank=True)
    subjects = models.ManyToManyField(Subject, related_name='books', blank=True)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={'pk': self.pk})
