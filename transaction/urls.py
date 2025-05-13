from django.urls import path
from .views import tran_list,tran_create


urlpatterns=[
    path('', tran_list, name='transaction_list'),
    path('create/',tran_create,name='tran_create'),
]