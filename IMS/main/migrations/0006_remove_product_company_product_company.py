# Generated by Django 4.2.1 on 2023-05-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_company_about_alter_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ManyToManyField(null=True, to='main.company', verbose_name='شرکت وابسته'),
        ),
    ]
