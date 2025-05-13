from django.urls import reverse_lazy
from django.views.generic import DeleteView

from book.models import Author


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete_author.html'
    success_url=reverse_lazy('author-list')
