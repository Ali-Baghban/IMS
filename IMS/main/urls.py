from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
urlpatterns = [
    path('', test, name='test'),
    path('dashboard', dashboard, name='dashboard'),
    path('users', users, name='users'),
    path('products', products, name='products'),
    path('product/update/<int:pid>', product_update, name='product_update'),
    path('product/delete/<int:pid>', product_delete, name='product_delete'),
    path('product/add', product_add, name='product_add'),
    path('settings', settings, name='settings'),

    path('login', login, name='login'),
    path('logout', logout, name='logout')
]