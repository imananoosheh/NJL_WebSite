# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-30 21:49
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='landingVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='MPV/', verbose_name='Video')),
                ('videoNum', models.IntegerField(editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title (Enlgish)')),
                ('slug', models.SlugField(editable=False, max_length=140, null=True, unique=True)),
                ('farsi_title', models.CharField(max_length=64, verbose_name='Title (Farsi)')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description (English)')),
                ('farsi_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description (Farsi)')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
    ]
