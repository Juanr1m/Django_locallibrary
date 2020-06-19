from django.urls import  path
from . import  views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name = 'authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView, name='author-detail')
]