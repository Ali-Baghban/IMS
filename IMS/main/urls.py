from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
urlpatterns = [
    path('', test, name='test'),
    path('dashboard', dashboard, name='dashboard'),
    path('users', users, name='users'),


    path('login', login, name='login'),
    path('logout', logout, name='logout')
]