# Generated by Django 4.1.7 on 2024-06-10 05:13

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_uz', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('name_ru', models.CharField(max_length=50, null=True)),
                ('view_home', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_uz', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('description_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('description_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('full_info', ckeditor.fields.RichTextField()),
                ('full_info_uz', ckeditor.fields.RichTextField(null=True)),
                ('full_info_en', ckeditor.fields.RichTextField(null=True)),
                ('full_info_ru', ckeditor.fields.RichTextField(null=True)),
                ('header_images', models.ImageField(blank=True, default='news/images/news.jpg', upload_to='news/images')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('category', models.ManyToManyField(related_name='category', to='news.category')),
                ('sub_category', models.ManyToManyField(blank=True, to='news.subcategory')),
            ],
            options={
                'ordering': ['-date'],
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
