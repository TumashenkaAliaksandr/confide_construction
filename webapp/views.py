from django.shortcuts import render
from webapp.models import Services, ServicesSlider, Recommended, Project, Callback
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import CallbackForm


def index(request):
    """Main, index constr"""
    serv = Services.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()

    context = locals()
    return render(request, 'webapp/index-2.html', context)



def services_slider(request):
    """Main, index constr"""
    servis_slider = ServicesSlider.objects.all()

    context = {
        'servis_slider': servis_slider,
    }
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
    return render(request, 'main/base.html', context=context)


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


def painting(request):
    """ Painting Constract"""
    return render(request, 'webapp/services/painting.html')


def project(request):
    """Projects for index Constract"""
    project_constract = Project.objects.all()
    main_project = Project.objects.filter(is_main=True).first()

    context = locals()
    return render(request, 'webapp/index-2.html', context)


def callback_view(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            # Создаем объект Callback и сохраняем его в базе данных
            callback = Callback(name=name, phone=phone)
            callback.save()

            # Отправка данных на почту
            message = f'Name: {name}\nPhone: {phone}'
            recipient_list = ['tumashenkaaliaksandr@gmail.com']  # Электронная почта получателя

            send_mail('Callback Request', message, 'your_email@gmail.com', recipient_list, fail_silently=False)

            # Перенаправление пользователя на страницу "спасибо"
            return redirect('webapp:home')

    else:
        form = CallbackForm()

    return render(request, 'webapp/forms/callback_form.html', {'form': form})



# def callback_view(request):
#     if request.method == 'POST':
#         form = CallbackForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone = form.cleaned_data['phone']
#
#             # Создаем объект Callback и сохраняем его в базе данных
#             callback = Callback(name=name, phone=phone)
#             callback.save()
#
#             # Отправка данных на почту
#             subject = 'Callback Request'
#             message = f'Name: {name}\nPhone: {phone}'
#             from_email = 'tumashenkaaliaksandr@gmail.com'  # Замените на вашу электронную почту
#             recipient_list = ['tumashenkaaliaksandr@gmail.com']  # Электронная почта получателя
#
#             try:
#                 send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#                 response_data = {'status': 'success'}
#             except Exception as e:
#                 response_data = {'status': 'error'}
#
#             return JsonResponse(response_data)
#
#     else:
#         form = CallbackForm()
#
#     return render(request, 'webapp/forms/callback_form.html', {'form': form})

