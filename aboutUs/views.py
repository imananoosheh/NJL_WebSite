from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from .models import content

def aboutUs(request):
    try:
        contents = content.objects.latest('id')
    except:
        contents = None
    context = {
        'content' : contents,
    }
    
    return render(request, 'about.html', context)
