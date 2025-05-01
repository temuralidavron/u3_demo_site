from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.models import RoleChoice


def muyasar_perm(func):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return func(request,*args, **kwargs)

    return wrapper




def admin_perm(func):
    def wrapper(request,*args,**kwargs):
        result=func(request,*args,**kwargs)
        if  request.user.is_authenticated:
            if request.user.role==RoleChoice.ADMIN:
                return result
        return HttpResponse("Sizga mumkin emas")
    return wrapper




