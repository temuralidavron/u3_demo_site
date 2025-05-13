from django import forms

from transaction.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['from_user','to_user','amount']



