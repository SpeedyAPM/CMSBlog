from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from taggit.models import Tag

from blog.models import BlogPost
from django.core.paginator import Paginator

# Create your views here.

def blog(request):
    blogs = BlogPost.objects.order_by('-created_on').all()
    tags = Tag.objects.all()
    p = Paginator(BlogPost.objects.order_by('-created_on').all(), 5)
    page = request.GET.get('page')
    pages = p.get_page(page)
    nums = "a"*pages.paginator.num_pages

    context = {'blogs': blogs, 'tags': tags, 'pages': pages, 'nums': nums}
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    tags = Tag.objects.all()
    context = {'blog': blog, 'tags': tags}
    return render(request, 'blogpost.html', context)


def search(request):
    return render(request, 'search.html')


def posts_by_tag(request, tag_slug):
    blogs = BlogPost.objects.filter(tags__slug=tag_slug)
    tags = Tag.objects.all()
    context = {'blogs': blogs, 'tags': tags}
    return render(request, 'bloghome.html', context)



