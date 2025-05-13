from django.urls import path
from accounts import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('forget/',views.forget_view,name='forget'),
    path('reset/',views.reset_password,name='reset'),
]