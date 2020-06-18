from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import article, category 

def article_detail(request, slug=None):
    try:
        instance = get_object_or_404(article, slug=slug)
    except ObjectDoesNotExist:
        instance = None
    context = {
        'article' : instance
    }
    return render(request, 'singlenewspage.html', context)

def All(request):
    try:
        All_articles = article.objects.all().order_by('-id')
        All_categories = category.objects.all().order_by('-id')
    except ObjectDoesNotExist:
        All_articles = None
        All_categories = None
    context = {
        'articles' : All_articles,
        'categories' : All_categories
    }
    return render(request, 'news.html', context)
