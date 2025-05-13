from django import forms
from django.forms import modelformset_factory

from book.models import Book, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'birth_date', 'country']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'price',
            'published_year',
            'file',
            'image',
        ]



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'country','birth_date']




