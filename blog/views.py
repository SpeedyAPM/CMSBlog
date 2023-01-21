from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from taggit.models import Tag

from blog.models import BlogPost
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def get_posts_page(posts, request):
    tags = Tag.objects.all()
    p = Paginator(posts, 5)
    page = request.GET.get('page')
    pages = p.get_page(page)
    context = {
        'tags': tags,
        'pages': pages,
        'nums': range(pages.paginator.num_pages)
    }
    return context


def blog(request):
    posts = BlogPost.objects.order_by('-created_on').all()
    context = get_posts_page(posts, request)
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    tags = Tag.objects.all()
    context = {'blog': blog, 'tags': tags}
    return render(request, 'blogpost.html', context)


def search(request):
    search_post = request.GET.get("search")

    if search_post:
        posts = BlogPost.objects.filter(
            Q(title__icontains=search_post) | Q(content__icontains=search_post) | Q(tags__name__icontains=search_post))
    else:
        posts = BlogPost.objects.all()

    posts = posts.order_by('-created_on')
    context = get_posts_page(posts, request)
    context["search"] = search_post
    return render(request, 'bloghome.html', context)


def posts_by_tag(request, tag_slug):
    posts = BlogPost.objects.filter(tags__slug=tag_slug).order_by("-created_on")
    return get_posts_page(posts, request)
