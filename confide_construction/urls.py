"""
URL configuration for confide_construction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from confide_construction.sitemaps import ProductSitemap, ServicesSitemap
from webapp.views import error404


sitemaps = {
    'products': ProductSitemap,
    'services': ServicesSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('', include('blog.urls')),
    path('payments/', include('payments.urls')),  # new
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

handler404 = error404
# handler404 = 'confide_construction.views.error404'
# handler500 = 'confide_construction.views.error500'
