from django.shortcuts import render
from blog.models import News


def blog(request):
    """these are views for Blog News list"""
    model_blog_main = News.objects.all()

    context = locals()
    return render(request, 'blog/blog-listing.html', context=context)


def NewsDetailView(request):
    """these are views for News list"""
    model = News.objects.all()

    context = locals()
    return render(request, 'blog/blog-details.html')


