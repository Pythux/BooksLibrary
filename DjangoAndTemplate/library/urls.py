from django.conf.urls import url
from . import views


author = [
    url(
        r'^author/$',
        views.AuthorListView.as_view(),
        name='author_list'),
    url(
        r'^author/(?P<pk>\d+)/$',
        views.AuthorDetailView.as_view(),
        name='author_detail'),
    url(
        r'^author/update/(?P<pk>\d+)/$',
        views.AuthorUpdateView.as_view(),
        name='author_update'),
    url(
        r'^author/delete/(?P<pk>\d+)/$',
        views.AuthorDeleteView.as_view(),
        name='author_delete'),
    url(
        r'^author/new/$',
        views.AuthorCreateView.as_view(),
        name='author_new'),
]

book = [
    url(
        r'^book/$',
        views.BookListView.as_view(),
        name='book_list'),
    url(
        r'^book/(?P<pk>[-\d]+)/$',
        views.BookDetailView.as_view(),
        name='book_detail'),
    url(
        r'^book/update/(?P<pk>[-\d]+)/$',
        views.BookUpdateView.as_view(),
        name='book_update'),
    url(
        r'^book/delete/(?P<pk>[-\d]+)/$',
        views.BookDeleteView.as_view(),
        name='book_delete'),
    url(
        r'^author/(?P<pk>[-\d]+)/book/$',
        views.add_book_to_author,
        name='book_new'),
    url(
        r'^book/new/$',
        views.BookCreateView.as_view(),
        name='book_new'),
]

subject = [
    url(
        r'^subject/$',
        views.SubjectListView.as_view(),
        name='subject_list'),
    url(
        r'^book/(?P<pk>[-\w]+)/$',
        views.SubjectDetailView.as_view(),
        name='subject_detail'),
    url(
        r'^subject/update/(?P<pk>[-\w]+)/$',
        views.SubjectUpdateView.as_view(),
        name='subject_update'),
    url(
        r'^subject/delete/(?P<pk>[-\w]+)/$',
        views.SubjectDeleteView.as_view(),
        name='subject_delete'),
    url(
        r'^subject/new/$',
        views.SubjectCreateView.as_view(),
        name='subject_new'),
]

urlpatterns = author + book + subject
