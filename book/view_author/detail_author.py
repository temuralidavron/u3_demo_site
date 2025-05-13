from django.views.generic import DetailView

from book.models import Author


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author/detail_author.html'