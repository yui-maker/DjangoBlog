# blog/views.py
from django.shortcuts import render
from .models import Content

def index(request):
    contents = Content.objects.all()
    return render(request, 'blog/index.html', {'contents': contents})

def category_view(request, category):
    contents = Content.objects.filter(category=category)
    return render(request, f'blog/{category}.html', {'contents': contents})
