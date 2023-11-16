from django.urls import path
from blog.views import blog, NewsDetailView

app_name = 'blog'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('single/<int:pk>/', NewsDetailView, name='single'),
]