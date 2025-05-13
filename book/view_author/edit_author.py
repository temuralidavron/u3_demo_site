from django.urls import reverse_lazy
from django.views.generic import UpdateView

from book.form import AuthorForm
from book.models import Author


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "author/author_create.html"
    success_url=reverse_lazy('author-list')