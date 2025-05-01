from django.urls import path

from .views import create_book, book_list, book_edit, book_delete, book_detail

urlpatterns = [
    path('',book_list, name='book-list'),
    path('create/',create_book,name='book-create'),
    path('edit/<int:pk>/',book_edit,name='book-edit'),
    path('delete/<int:pk>/',book_delete,name='book-delete'),
    path('detail/<int:pk>/',book_detail,name='book-detail'),

    #author crud

]