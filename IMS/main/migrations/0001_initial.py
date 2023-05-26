# Generated by Django 4.2.1 on 2023-05-26 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, verbose_name='نام شرکت')),
                ('about', models.TextField(blank=True, default=None, verbose_name='درباره ما')),
                ('website', models.CharField(blank=True, default='https://google.com', max_length=200, verbose_name='وبگاه شرکت')),
                ('web_id', models.CharField(blank=True, default=None, max_length=100, verbose_name='نام کاربری شرکت')),
                ('public', models.BooleanField(default=False, verbose_name='قابل رویت برای دیگران')),
                ('logo', models.ImageField(blank=True, default='company_logo/default_logo.png', upload_to='company_logo/', verbose_name='نمایه')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='ناشناس', max_length=100, verbose_name='نام کاربر')),
                ('bio', models.TextField(blank=True, default=None, verbose_name='بیوگرافی')),
                ('admin', models.BooleanField(choices=[(True, 'مدیر'), (False, 'پرسنل')], default=False, verbose_name='مدیر')),
                ('phone', models.IntegerField(blank=True, default=None, verbose_name='شماره همراه')),
                ('salary', models.IntegerField(blank=True, default=None, verbose_name='درامد ماهیانه')),
                ('avatar', models.ImageField(blank=True, default='profile_images/default.png', upload_to='profile_images/', verbose_name='نمایه')),
                ('company', models.ManyToManyField(to='main.company', verbose_name='وابستگی شرکتی')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, verbose_name='نام محصول')),
                ('type', models.CharField(choices=[('countable', 'عددی'), ('Noncountable', 'مقداری')], default='عددی', max_length=20, verbose_name='نوع محصول')),
                ('count', models.IntegerField(blank=True, default=0, verbose_name='مقدار/تعداد')),
                ('price', models.IntegerField(blank=True, default=None, verbose_name='قیمت')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.company', verbose_name='شرکت وابسته')),
            ],
        ),
    ]