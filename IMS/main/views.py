from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_view
from django.contrib import auth
from .models import *


def test(request):
    return redirect('dashboard')

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
    company         = get_object_or_404(Company,person=user)
    products        = Product.objects.all().filter(company=company)

    context = {
        'company' : company,
        'products': products,

    }
    return render(request, 'main/dashboard.html', context=context)

def users(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
    company         = get_object_or_404(Company,person=user)
    personal        = Profile.objects.all().filter(company=company)

    context = {
        'company' : company,
        'personal': personal,
    }
    return render(request, 'main/users.html', context=context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'main/login.html')
        

def logout(request):
    return auth_view.logout_then_login(request,)
