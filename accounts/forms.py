from django import forms
from .models import CustomUser
# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import check_password
# # from django.contrib.auth.models import User
# from django.http import HttpResponse



class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        ]

    # def save(self,commit=True,*args, **kwargs):
    #     return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput,max_length=50)


    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if len(password)!=3:
    #         return password
    #     else:
    #         raise forms.ValidationError("203 Bad password")
    #
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if username:
    #         return username
    #     else:
    #         raise forms.ValidationError("203 Bad password")
    #

    #
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(request, username=username, password=password)










        # if not  user:
        #     check_password(password, user.password)
        #     return HttpResponse("403 Forbidden")
        # return {'user': user}


class ForgetForm(forms.Form):
    username = forms.CharField(max_length=40)


class ResetForm(forms.Form):
    code = forms.CharField(max_length=6)
    password = forms.CharField(max_length=50)
    re_password = forms.CharField(max_length=50)