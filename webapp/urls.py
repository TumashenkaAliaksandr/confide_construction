from django.urls import path

from . import views
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


app_name = 'webapp'


urlpatterns = [
    path('', index, name='home'),
    path('services/', services, name='services'),  # Паттерн без slug
    path('services/<slug:slug>/', single_product, name='services_with_slug'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('invoices/', invoices, name='invoices'),
    path('invoices/<slug:slug>/', single_invoices, name='invoices_with_slug'),
    path('stata', stata, name='stata'),
    path('send-invoice/', send_invoice, name='send_invoice'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('backsplash/', backsplash, name='backsplash'),
    path('drywall/', drywall, name='drywall'),
    path('disposal/', disposal, name='disposal'),
    path('ceiling-fan/', ceiling_fan, name='ceiling-fan'),
    path('handyman/', handyman, name='handyman'),
    path('tv-mount/', tv_mount, name='tv-mount'),
    path('furniture-assembly/', furniture, name='furniture-assembly'),
    path('wallpaper/', wallpaper, name='wallpaper'),
    path('painting/', painting, name='painting'),
    path('soundproofing/', soundproofing, name='soundproofing'),
    path('electricalworks/', electricalworks, name='electricalworks'),
    path('profiler/', shop, name='profiler'),
    # path('shop/<slug>', single_product, name='single_product'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('register/', registration, name='register'),
    path('process_payment/', process_payment, name='process_payment'),
    path('error/', error404, name='error'),
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
    path('basket/', basket_detail, name='basket_detail'),
    path('add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('basket/update/<int:item_id>/', update_basket, name='update_basket'),
    path('basket/remove/<int:item_id>/', remove_from_basket, name='remove_from_basket'),
    path('order/', views.order_view, name='order_view'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
