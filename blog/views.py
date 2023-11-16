from django.shortcuts import render
from blog.models import *
from django.shortcuts import render, get_object_or_404


def blog(request):
    """these are views for Blog News list"""
    model_blog_main = BlogNews.objects.all()

    context = locals()
    return render(request, 'blog/blog-listing.html', context=context)


def NewsDetailView(request, pk):
    """Views for News details"""
    news = BlogNews.objects.filter(pk=pk)
    context = {'news': news}
    return render(request, 'blog/blog-details.html', context=context)


