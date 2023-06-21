from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_view
from django.contrib import auth
from .models import *
from home.models import News
from django.http import HttpResponse
import time


def test(request):
    return redirect('dashboard')

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        print(user_id)
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
    company         = get_object_or_404(Company,person=user)
    products        = Product.objects.all().filter(company=company)
    news            = News.objects.all()[:3]
    context = {
        'company' : company,
        'products': products,
        'news': news

    }
    return render(request, 'main/dashboard.html', context=context)
@login_required
def users(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
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

@login_required       
def logout(request):
    return auth_view.logout_then_login(request,)

@login_required
def user_delete(request,pid):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
        company     = get_object_or_404(Company,person=user)
        if Profile.objects.filter(company=company,pk=pid).delete():
            return redirect('users')
        else:
            return redirect('prodcut_apdate'+pid)

# Need to update #
@login_required
def user_update(request,pid):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
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
        profile = Profile.objects.filter(company=company,pk=pid).get()
        context = {
            'profile' : profile,
        }
        return render(request, 'main/product.html', context=context)

# Product tasks :)
@login_required
def products(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
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
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
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
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
        company     = get_object_or_404(Company,person=user)
        if Product.objects.filter(company=company,pk=pid).delete():
            return redirect('products')
        else:
            return redirect('prodcut_apdate'+pid)

@login_required
def product_add(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
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

# Setting tasks :)
@login_required
def settings(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
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

# Company Tasks :)

def register_company(request):
    # Registration User
    if request.method == 'POST':
        first_name  = request.POST['firstname']
        last_name   = request.POST['lastname']
        email       = request.POST['email']
        username    = request.POST['username']
        password    = request.POST['password']
        repassword  = request.POST['repassword']
        if len(password) | len(repassword) < 8 :
            return redirect('register_company')
        else:
            if password != repassword : 
                return redirect('register_company')
            else:
                if  User.objects.filter(username=username).exists():
                    return redirect('register_company')
                else:
                    if User.objects.filter(email=email).exists():
                        return redirect('register_company')
                    else:
                        user = User.objects.create_user(
                            username=username, password=password, email=email, first_name=first_name,
                            last_name=last_name
                        )
                        user.save()
                        #return redirect('login')
        
        name    = first_name+' '+last_name
        bio     = request.POST['bio']
        admin   = True
        phone   = request.POST['phone']
        salary  = request.POST['salary']

        profile = Profile.objects.create(name=name,
                                         bio=bio,
                                         admin=admin,
                                         phone=phone,
                                         salary=salary,
                                         user=user
                                         )
        #profile.user.add(user)
        profile.save()
        print(profile.id)
        name    = request.POST['company_name']
        about   = request.POST['about']
        website = request.POST['website']
        web_id  = request.POST['web_id']
        #print(name, about, website, web_id)
        company = Company.objects.create(name=name,
                                         about=about,
                                         website=website,
                                         web_id=web_id,
                                         )
        company.person.add(profile)
        company.save()


        return redirect('login')

    else:
        return render(request, 'main/register_company.html')



def report_writer(data, option):
    time    = time.datetime.now()
    options = {'add': 'افزودن', 'edit': 'تغییر', 'delete': 'حذف'}
    report  = options[option] + data
    return report

@login_required
def report_products(request):
    if request.user.is_authenticated:
        user_id     = request.user.id
        user        = get_object_or_404(User,id=user_id)
        user        = get_object_or_404(Profile, user=user)
    company         = get_object_or_404(Company,person=user)
    products        = Product.objects.all().filter(company=company)
    context = {
        'company' : company,
        'products': products,
    }
    return render(request, 'main/report.html', context=context)
