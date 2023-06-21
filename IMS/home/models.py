from django.db import models
from PIL import Image
class Slider(models.Model):

    title   = models.CharField(max_length=100, blank=True, verbose_name='عنوان')
    caption = models.TextField(verbose_name='متن', blank=True) 
    photo   = models.ImageField(upload_to='slider/%Y/%m/%d/', verbose_name='تصویر')
    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'
    def __str__(self):
        return self.title

class Blog(models.Model):
    title   = models.CharField(max_length=100, blank=True, verbose_name='عنوان')
    body    = models.TextField(verbose_name='متن', blank=True) 
    photo   = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='تصویر')

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'
    def __str__(self):
        return self.title

class About(models.Model):

    name    = models.CharField(max_length=100, blank=True, verbose_name='نام')
    caption = models.TextField(verbose_name='متن', blank=True) 
    photo   = models.ImageField(upload_to='about/%Y/%m/%d/', verbose_name='تصویر')
    link    = models.CharField(max_length=150, blank=True, verbose_name='لینک')
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
    def __str__(self):
        return self.name
    
class News(models.Model):

    title   = models.CharField(max_length=100, blank=True, verbose_name='عنوان')
    body    = models.TextField(verbose_name='متن', blank=True) 
    photo   = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='تصویر')
# resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 100 or img.width > 100:
            new_img = (450, 300)
            img.thumbnail(new_img)
            img.save(self.photo.path)
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
    def __str__(self):
        return self.title