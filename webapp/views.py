from django.shortcuts import render
from webapp.models import Services, ServicesSlider, Recommended, Project


def index(request):
    """Main, index constr"""
    serv = Services.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()

    context = locals()
    return render(request, 'webapp/index-2.html', context)


def slider_services(request):
    """Main, index constr"""
    serv_slider = ServicesSlider.objects.all()

    context = {'serv_slider': serv_slider}
    return render(request, 'webapp/services.html', context)


def services(request):
    """Services Constract"""
    serv_serv = Services.objects.all()
    main_ser = Services.objects.filter(is_main=True).first()
    sl_serv = Services.objects.all()

    context = locals()
    return render(request, 'webapp/services.html', context)


def recommended(request):
    """Main, recommended constr"""
    company = Recommended.objects.all()
    main_company = Recommended.objects.filter(is_main=True).first()

    context = {
        'company': company,
        'main_company': main_company,
    }
    return render(request, 'webapp/contact-us-1.html', context=context)


def shop(request):
    """Shop Constract"""
    return render(request, 'webapp/shop.html')


def about(request):
    return render(request, 'webapp/about-us.html')


def contacts(request):
    return render(request, 'webapp/contact-us-1.html')


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


def furniture(request):
    """Furniture Assembly Constract"""
    return render(request, 'webapp/services/furniture_assembly.html')


def project(request):
    """Projects for index Constract"""
    project_constract = Project.objects.all()
    main_project = Project.objects.filter(is_main=True).first()

    context = locals()
    return render(request, 'webapp/index-2.html', context)
