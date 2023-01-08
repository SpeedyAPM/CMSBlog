from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from blog.models import Blog

# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request, 'blogpost.html', context)

def search(request):
    return render(request, 'search.html')

