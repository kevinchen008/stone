from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.template import Template
from django.utils._os import safe_join
import os

# Create your views here.


def get_pages_or_404(name):
    try:
        file_path = safe_join(settings.BASE_STONE_WEB_DIR,name)
    except ValueError:
        raise Http404('Page not found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page not found')
    with open (file_path,'r') as f:
         page = Template(f.read())
    return page

def page(request,slug='index'):
    file_name = '{}.html'.format(slug)
    page = get_pages_or_404(file_name)
    context = {
        'slug':slug,
        'page':page
    }
    return render(request,'page.html',context)



def login(request):
    return render(request,'login.html')