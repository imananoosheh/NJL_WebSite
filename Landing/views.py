from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from .models import sections,landingVideo
from newsApp.models import article,category

def Home(request):
    try:
        All_Sections = sections.objects.all()
        All_articles = article.objects.all().order_by('-id')[:3]
        All_categories = category.objects.all()
        All_videos = landingVideo.objects.all()
    except ObjectDoesNotExist:
        All_Sections = None
        All_articles = None
        All_categories = None
        All_videos = None

    context = {
        'sections' : All_Sections,
        'categories' : All_categories,
        'articles' : All_articles,
        'vidsPics' : All_videos
    }
    
    return render(request, 'index.html', context)
