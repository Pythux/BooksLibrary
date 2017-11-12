from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^books$', views.book_list),
    url(r'^books/(?P<pk>[-\d]+)$', views.book_detail),
]
