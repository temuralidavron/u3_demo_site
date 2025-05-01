from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,redirect

from book.form import BookForm
from book.models import Book, Author
from .utils import muyasar_perm,admin_perm

# @permisson_required()
# @admin_perm
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(request.POST)
    return render(request, 'book/book_form.html', {'form': form})





def book_list(request):
    books = Book.objects.all()
    q=request.GET.get('q')
    if q:
        books = books.filter(Q(title__icontains=q) | Q(description__icontains=q))
    else:
        books = books.all()
    books = books.order_by('title')
    paginator = Paginator(books, 2)
    page = request.GET.get('page',1)
    books = paginator.get_page(page)
    return render(request, 'book/book_list.html', {'books': books})

# @permission_required("book.view_book",raise_exception=True)
def book_detail(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_edit(request,pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        form=BookForm(request.POST ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form=BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})


def book_delete(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book-list')
    else:
        return render(request, 'book/book_delete.html', {'book': book})



