from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import News


def blog(request):
    return render(request, 'blog/blog-listing.html')


class NewsListView(ListView):
    """these are views for News list"""
    model = News
    template_name = 'blog/blog-listing.html'
    context_object_name = 'news_list'
    paginate_by = 5
    ordering = ['-pub_date']

class NewsDetailView(ListView):
    """these are views for News list"""
    model = News
    template_name = 'blog/blog-details.html'
    context_object_name = 'news_detail'
    ordering = ['-pub_date']