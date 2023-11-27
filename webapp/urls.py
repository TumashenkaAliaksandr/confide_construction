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
    path('checkout/', checkout, name='checkout'),
    path('login/', CRloginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register_done/', registerdone, name='register_done'),
    # path('send_email/', send_email, name='send_email'),
    path('search/', Search.as_view(), name='search'),
    path('my_account/', my_account, name='my_account'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
