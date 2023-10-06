from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from webapp.models import Services, ServicesSlider, Recommended, Project, Callback
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import CallbackForm, PaymentForm
from django.http import JsonResponse
import stripe


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

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Получите данные из формы
            order = form.cleaned_data['order']
            payment_amount = form.cleaned_data['payment_amount']
            payment_method = form.cleaned_data['payment_method']
            expiration_date_month = form.cleaned_data['expiration_date_month']
            expiration_date_year = form.cleaned_data['expiration_date_year']

            # Создайте Stripe токен (необходимо подключить Stripe.js для этого)
            try:
                token = stripe.Token.create(
                    card={
                        "number": form.cleaned_data['card_number'],
                        "exp_month": expiration_date_month,
                        "exp_year": expiration_date_year,
                        "cvc": form.cleaned_data['cvv'],
                    },
                )

                # Создайте платеж в Stripe
                charge = stripe.Charge.create(
                    amount=int(payment_amount * 100),  # Сумма в центах
                    currency='usd',
                    source=token.id,
                    description=f'Payment for Order #{order}',
                )

                # Обработка успешного платежа
                return JsonResponse({'success': True, 'message': 'Payment successful. Your order has been confirmed.'})
            except stripe.error.StripeError as e:
                # Обработка ошибок Stripe
                return JsonResponse({'success': False, 'message': f'Payment failed: {str(e)}'})

    else:
        form = PaymentForm()

    return render(request, 'webapp/index.html', {'form': form})


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

