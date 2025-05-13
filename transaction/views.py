from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

from transaction.forms import TransactionForm
from transaction.models import Transaction


def tran_list(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'transaction/transaction_list.html', context)

@transaction.atomic
def tran_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            from_user = form.cleaned_data['from_user']
            to_user = form.cleaned_data['to_user']
            amount = form.cleaned_data['amount']
            if from_user.balance < amount:
                return HttpResponse("Muyassar o'g'rincha pul olmang")
            from_user.balance -= amount
            from_user.save()
            to_user.balance += amount
            to_user.save()
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
        return render(request, 'transaction/transaction_create.html', {'form': form})
