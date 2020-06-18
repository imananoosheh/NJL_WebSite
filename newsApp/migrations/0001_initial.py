# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-30 21:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import newsApp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True, verbose_name='Title (English)')),
                ('slug', models.SlugField(editable=False, max_length=140, null=True, unique=True)),
                ('farsiTitle', models.CharField(max_length=64, null=True, verbose_name='Title (Farsi)')),
                ('shortDescription', models.TextField(max_length=400, null=True, verbose_name='Short Description (English)')),
                ('farsiShortDescription', models.TextField(max_length=400, null=True, verbose_name='Short Description (Farsi)')),
                ('articleImage', models.ImageField(upload_to='news/', validators=[newsApp.validators.validate_file_extension_coverImage], verbose_name='Cover Photo')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Description (English)')),
                ('farsiDescription', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Description (Farsi)')),
                ('date', models.CharField(max_length=64, null=True, verbose_name='Date')),
                ('Farsidate', models.CharField(max_length=64, null=True, verbose_name='Jalali Date')),
                ('authorName', models.CharField(max_length=64, null=True, verbose_name='Author Name (English)')),
                ('farsiAuthoName', models.CharField(max_length=64, null=True, verbose_name='Author Name (Farsi)')),
            ],
            options={
                'verbose_name_plural': 'Article',
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farsiName', models.CharField(max_length=64, verbose_name='Name (English)')),
                ('name', models.CharField(max_length=64, verbose_name='Name (Farsi)')),
                ('slug', models.SlugField(editable=False, max_length=140, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='newsApp.category', verbose_name='Categories'),
        ),
    ]
