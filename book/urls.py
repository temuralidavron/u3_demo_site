from django.urls import path

from .view_author.author_list import AuthorListView
from .view_author.create_author import AuthorCreate
from .view_author.delete_author import AuthorDeleteView
from .view_author.detail_author import AuthorDetailView
from .view_author.edit_author import AuthorUpdateView
from .views import create_book, book_list, book_edit, book_delete, book_detail, send_html_view

urlpatterns = [
    path('',book_list, name='book-list'),
    path('create/',create_book,name='book-create'),
    path('edit/<int:pk>/',book_edit,name='book-edit'),
    path('delete/<int:pk>/',book_delete,name='book-delete'),
    path('detail/<int:pk>/',book_detail,name='book-detail'),

    #author crud
    path("author/create/",AuthorCreate.as_view(),name="author-create"),
    path("author/list/",AuthorListView.as_view(),name="author-list"),
    path("author/detail/<int:pk>/",AuthorDetailView.as_view(),name="author-detail"),
    path("author/update/<int:pk>/",AuthorUpdateView.as_view(),name="author-update"),
    path("author/delete/<int:pk>/",AuthorDeleteView.as_view(),name="author-delete"),
    # email
    path("send/",send_html_view),
]