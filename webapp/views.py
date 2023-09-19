from django.shortcuts import render

from webapp.models import *

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
    serv_serv = Services.objects.all()
    main_ser = Services.objects.filter(is_main=True).first()

    context = {
        'serv_serv': serv_serv,
        'main_ser': main_ser,
    }
    return render(request, 'webapp/services.html', context=context)

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

def wallpaper(request):
    """Wallpaper Constract"""
    return render(request, 'webapp/services/wallpaper.html')

def soundproofing(request):
    """Soundproofing Constract"""
    return render(request, 'webapp/services/soundproofing.html')


