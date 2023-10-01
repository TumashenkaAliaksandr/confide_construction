from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('services/', services, name='services'),
    path('services_slider/', services_slider, name='services_slider'),
    path('backsplash/', backsplash, name='backsplash'),
    path('drywall/', drywall, name='drywall'),
    path('handyman/', handyman, name='handyman'),
    path('furniture-assembly/', furniture, name='furniture-assembly'),
    path('wallpaper/', wallpaper, name='wallpaper'),
    path('painting/', painting, name='painting'),
    path('soundproofing/', soundproofing, name='soundproofing'),
    path('electricalworks/', electricalworks, name='electricalworks'),
    path('projects/', project, name='projects'),
    path('shop/', shop, name='shop'),
    path('recommended/', recommended, name='recommended'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('callback/', callback_view, name='callback'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
