from django.urls import path,include
from users.views import (login)
from django.conf.urls import url
from django.views import generic


app_name='users'
urlpatterns=[
    path(r'login',login,name='login'),
    path(r'register',register,name='register'),
]