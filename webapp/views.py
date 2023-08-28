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
    serv = Services.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()

    context = {
        'serv': serv,
        'main_serv': main_serv,
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
