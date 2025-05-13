from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView

from book.form import AuthorForm
from book.models import Author


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    success_url =reverse_lazy("author-list")
    template_name = 'author/author_create.html'

