from django.urls import path
from blog.views import *
from webapp.views import NewsListView


app_name = 'blog'


urlpatterns = [
    path('blog/', NewsListView.as_view(), name='blog'),
    path('single/<int:pk>/', NewsListView.as_view(), name='single'),
]