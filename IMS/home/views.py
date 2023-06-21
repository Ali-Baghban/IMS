from django.shortcuts import render
from .models import *

def index(request):
    sliders = Slider.objects.all()
    about   = About.objects.all()[:2]
    blogs   = Blog.objects.all()
    context= {
        'sliders':sliders,
        'about':about,
        'blogs':blogs

    }
    return render(request, 'home/index.html', context=context)