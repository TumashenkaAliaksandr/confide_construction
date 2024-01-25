from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


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
    path('register/', registration, name='register'),
    path('process_payment/', process_payment, name='process_payment'),
    path('error/', error, name='error'),
    path('checkout/', checkout, name='checkout'),
    path('login/', CRloginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register_done/', registerdone, name='register_done'),
    path('search/', Search.as_view(), name='search'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('update_profile/<int:pk>/', UpdateProfilePageView.as_view(), name='update_profile'),
    path('my_account/', my_account, name='my_account'),
    path('comingsoon/', comingsoon, name='comingsoon'),
    path('lost_password/', lost_password, name='lost_password'),
    path('success/', success, name='success'),
    path('order_exists/', order_exists, name='order_exists'),
    path('order_error/', order_error, name='order_error'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
