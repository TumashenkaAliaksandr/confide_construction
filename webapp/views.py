from django.shortcuts import render
from webapp.models import *


def main_menu(request):
    active_menu_item = None  # По умолчанию нет активного элемента меню

    # Определите текущий URL и присвойте соответствующий элемент меню
    current_url_name = request.resolver_match.url_name
    if current_url_name in ['backsplash', 'drywall', 'handyman', 'electricalworks']:
        active_menu_item = 'services'

    # Определите элементы меню и передайте их в шаблон
    menu_items = [
        ('home', 'Home'),
        ('services', 'Services'),
        ('backsplash', 'Backsplash'),
        ('drywall', 'Drywall'),
        ('electricalworks', 'Electricalworks'),
        ('handyman', 'Handyman'),
        ('contacts', 'Contacts'),
        # Добавьте другие элементы меню, если необходимо
    ]

    return render(request, 'main/base.html', {'active_menu_item': active_menu_item})




def index(request):
    """Main, index constr"""
    serv = Services.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()

    context = {
        'serv': serv,
        'main_serv': main_serv,
    }
    return render(request, 'webapp/index-2.html', context=context)

def services(request):
    """Services Constract"""
    return render(request, 'webapp/services.html')

def shop(request):
    """Shop Constract"""
    return render(request, 'webapp/shop.html')

def about(request):
    return render(request, 'webapp/about-us.html')

def contacts(request):
    return render(request, 'webapp/contact-us-1.html')

def recommended(request):
    """Main, recommended constr"""
    company = Services.objects.all()
    main_company = Services.objects.filter(is_main=True).first()

    context = {
        'company': company,
        'main_company': main_company,
    }
    return render(request, 'webapp/index-2.html', context=context)


def backsplash(request):
    """Backsplash Constract"""
    return render(request, 'webapp/services/backsplash.html')

def drywall(request):
    """Drywall Constract"""
    return render(request, 'webapp/services/drywall.html')

def electricalworks(request):
    """Electricalworks Constract"""
    return render(request, 'webapp/services/electricalworks.html')

def handyman(request):
    """Handyman Constract"""
    return render(request, 'webapp/services/handyman.html')
