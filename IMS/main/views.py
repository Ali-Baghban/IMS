from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_view
from django.contrib import auth
from .models import *
from django.http import HttpResponse


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
@login_required
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
@login_required
def products(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
    company         = get_object_or_404(Company,person=user)
    products        = Product.objects.all().filter(company=company)
    context = {
        'company' : company,
        'products': products,
    }
    return render(request, 'main/products.html', context=context)

@login_required
def product_update(request,pid):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
        company     = get_object_or_404(Company,person=user)
    if request.method == 'POST':
        name        = request.POST['name']
        price       = request.POST['price']
        count       = request.POST['count']
        type       = request.POST['type']
        if Product.objects.filter(company=company,pk=pid).update(name=name,count=count,price=price,type=type):
            return redirect('products')
        else:
            return redirect('prodcut_apdate'+pid)
    else:
        product = Product.objects.filter(company=company,pk=pid).get()
        context = {
            'product' : product,
        }
        return render(request, 'main/product.html', context=context)

@login_required
def product_delete(request,pid):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
        company     = get_object_or_404(Company,person=user)
        if Product.objects.filter(company=company,pk=pid).delete():
            return redirect('products')
        else:
            return redirect('prodcut_apdate'+pid)

@login_required
def product_add(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
        company     = get_object_or_404(Company,person=user)
    if request.method == 'POST':
        name        = request.POST['name']
        price       = request.POST['price']
        count       = request.POST['count']
        type        = request.POST['type']
        p = Product.objects.create(name=name,count=count,price=price,type=type)
        p.company.add(company)
        return redirect('products')
    else:
        return render(request, 'main/product_add.html')


@login_required
def settings(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(Profile,id=user_id)
        company         = get_object_or_404(Company,person=user)
    if request.method == 'POST':
        name        = request.POST['name']
        web_id      = request.POST['web_id']
        website     = request.POST['website']
        about       = request.POST['about']
        public      = bool(request.POST.get('public', False))
        print(type(about))
        Company.objects.filter(person=user).update(name=name,web_id=web_id,website=website,about=about,public=public)
        return redirect('settings')
    else:
        context = {
            'company' : company,
        }
        return render(request, 'main/settings.html', context=context)

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
