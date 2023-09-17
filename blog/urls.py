from django.urls import path
from blog.views import *


app_name = 'blog'


urlpatterns = [
    path('blog/', NewsListView.as_view(), name='blog'),
    path('single/', NewsDetailView.as_view(), name='single'),

]