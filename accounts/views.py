from django.utils import timezone

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from book.views import send_html_view
from .forms import UserForm, LoginForm, ForgetForm, ResetForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Code, CustomUser


# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    else:
        form=UserForm()


    return render(request,'accounts/register.html',{'form':form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:  # User topilganligini tekshirish
                login(request, user)
                return redirect('book-list')
            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            return HttpResponse('Form is not valid', status=400)
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


def forget_view(request):
    if request.method == 'POST':
        form = ForgetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = CustomUser.objects.filter(username=username).first()
            if user is not None:
                code=Code.objects.create(user=user)
                send_html_view(
                    request,
                    subject="Parollingizni o'zgartiring",
                    to_email=user.email,
                    code=code.code,
                    username=user.username
                )
                return render(request, 'accounts/forget.html', {'form': form})

    return render(request, 'accounts/forget_password.html', {'form': ForgetForm()})



def reset_password(request):
    name = request.GET.get('name')
    if request.method=='POST':
        form=ResetForm(request.POST)
        if form.is_valid():
            user=CustomUser.objects.filter(username=name).first()
            if user is not None:
                code=form.cleaned_data.get('code')
                user_code=Code.objects.filter(user=user,expire_date__gt=timezone.now()).first()
                print(code)
                if code!=user_code.code:
                    return HttpResponse("Code xat boshqattan urining!!!")
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                return redirect("login")
    else:
        form=ResetForm()
    return render(request,'accounts/done_reset.html',{'form':form})