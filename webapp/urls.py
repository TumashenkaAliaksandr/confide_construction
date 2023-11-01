from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('services/', services, name='services'),
    path('backsplash/', backsplash, name='backsplash'),
    path('drywall/', drywall, name='drywall'),
    path('disposal/', disposal, name='disposal'),
    path('handyman/', handyman, name='handyman'),
    path('furniture-assembly/', furniture, name='furniture-assembly'),
    path('wallpaper/', wallpaper, name='wallpaper'),
    path('painting/', painting, name='painting'),
    path('soundproofing/', soundproofing, name='soundproofing'),
    path('electricalworks/', electricalworks, name='electricalworks'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('callback/', callback_view, name='callback'),
    path('register/', registration, name='register'),
    path('process_payment/', process_payment, name='process_payment'),
    path('error/', error, name='error'),
    path('events/', events, name='events'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
