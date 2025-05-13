from django.views.generic import ListView

from book.models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'
    context_object_name='authors'

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['salom']='issiq'
        return context


# http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']