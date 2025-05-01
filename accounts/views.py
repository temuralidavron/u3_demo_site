from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


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