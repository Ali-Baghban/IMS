# Generated by Django 4.2.1 on 2023-05-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_product_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ManyToManyField(blank=True, to='main.company', verbose_name='شرکت وابسته'),
        ),
    ]