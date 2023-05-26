from django.db import models
from django.contrib.auth .models import User
from PIL import Image


class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    #company         = models.ManyToManyField('Company', verbose_name='وابستگی شرکتی')
    name            = models.CharField(max_length=100, default='ناشناس', blank=True, verbose_name='نام کاربر')
    bio             = models.TextField(blank=True, null=True, verbose_name='بیوگرافی')
    LEVEL_CHOICE    = [(True,'مدیر'),(False,'پرسنل')]
    admin           = models.BooleanField(default=False, choices=LEVEL_CHOICE, verbose_name='مدیر')
    phone           = models.CharField(max_length=20, null=True, blank=True, verbose_name='شماره همراه')
    salary          = models.IntegerField(null=True, blank=True, verbose_name='درامد ماهیانه')
    avatar          = models.ImageField(default='profile_images/default.png', upload_to='profile_images/', blank=True, verbose_name='نمایه')

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    def __str__(self):
        return self.name

class Company(models.Model):
    name            = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام شرکت')
    person          = models.ManyToManyField('Profile', verbose_name='کاربران')
    about           = models.TextField(blank=True, null=True, verbose_name='درباره ما')
    website         = models.CharField(max_length=200, default='https://google.com', blank=True, verbose_name='وبگاه شرکت')
    web_id          = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام کاربری شرکت')
    public          = models.BooleanField(default=False, verbose_name='قابل رویت برای دیگران')
    logo            = models.ImageField(default='company_logo/default_logo.png', upload_to='company_logo/', blank=True, verbose_name='نمایه')

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.logo.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.logo.path)
    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'
    def __str__(self):
        return self.name
    
class Product(models.Model):
    company         = models.ManyToManyField('Company', null=True, verbose_name='شرکت وابسته')
    name            = models.CharField(max_length=100, default=None, blank=True, verbose_name='نام محصول')
    TYPE_CHOICE     = [('countable','عددی'),('Noncountable','مقداری')]
    type            = models.CharField(max_length=20, default='عددی', choices=TYPE_CHOICE, verbose_name='نوع محصول')
    count           = models.IntegerField(default=0, blank=True, verbose_name='مقدار/تعداد')
    price           = models.IntegerField(default=None, blank=True, verbose_name='قیمت')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    def __str__(self):
        return self.name