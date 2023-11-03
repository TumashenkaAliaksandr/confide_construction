from django.views.decorators.csrf import csrf_exempt
from webapp.models import *
from django.core.mail import send_mail
from .forms import CallbackForm, PaymentForm, RegistrationForm, ContactForm
from django.http import JsonResponse, HttpResponse
import stripe
from django.contrib.auth import login
from django.shortcuts import render, redirect


def index(request):
    """Main, index constr"""
    serv = Services.objects.all()
    partner = Recommended.objects.all()
    project_constract = Project.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()

    context = locals()
    return render(request, 'webapp/index-2.html', context)


def services(request):
    """Services Constract"""
    serv_serv = Services.objects.all()
    servis_slider = ServicesSlider.objects.all()
    main_ser = Services.objects.filter(is_main=True).first()
    sl_serv = Services.objects.all()

    context = locals()
    return render(request, 'webapp/services.html', context)


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

    return render(request, 'webapp/cart.html', {'form': form})


def about(request):
    assessment = Assessment.objects.all()
    partner = Recommended.objects.all()
    servis_sliders = ServicesSlider.objects.all()

    context = {
        'assessment': assessment,
        'partner': partner,
        'servis_sliders': servis_sliders,
    }
    return render(request, 'webapp/about-us.html', context=context)


# @csrf_exempt
# def send_email(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#         try:
#             send_mail('Subject', message, email, ['tumashenkaaliaksandr@gmail.com'], fail_silently=False)
#             response_data = {'signal': 'ok', 'msg': 'Message sent successfully.'}
#             return JsonResponse(response_data)
#         except Exception as e:
#             response_data = {'signal': 'error', 'msg': str(e)}
#             return JsonResponse(response_data)
#     else:
#         return HttpResponse(status=400)  # Return a Bad Request response if the request is not a POST request


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Здесь отправляем письмо
            send_mail(
                subject='New Contact Form Submission',
                message=message,
                from_email=email,
                recipient_list=['tumashenkaaliaksandr@gmail.com'],  # Замените на ваш адрес получателя
                fail_silently=False,
            )

            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'webapp/contact-us-1.html', context=context)


def login(request):
    return render(request, 'webapp/login.html')



def backsplash(request):
    """Backsplash Constract"""
    return render(request, 'webapp/services/backsplash.html')


def drywall(request):
    """Drywall Constract"""
    disp_obj = Drywall.objects.all()
    main_serv = Services.objects.all()

    context = locals()
    return render(request, 'webapp/services/drywall.html', context)

def disposal(request):
    """Disposal Constract"""
    disp_obj = DisposalService.objects.all()
    main_serv = Services.objects.all()

    context = locals()

    return render(request, 'webapp/services/disposal.html', context)


def electricalworks(request):
    """Electricalworks Constract"""
    return render(request, 'webapp/services/electricalworks.html')


def handyman(request):
    """Handyman Constract"""
    return render(request, 'webapp/services/handyman.html')


def wallpaper(request):
    """Wallpaper Constract"""
    disp_obj = DisposalService.objects.all()
    main_serv = Services.objects.all()

    context = locals()

    return render(request, 'webapp/services/wallpaper.html', context=context)


def soundproofing(request):
    """Soundproofing Constract"""
    disp_obj = DisposalService.objects.all()
    main_serv = Services.objects.all()

    context = locals()
    return render(request, 'webapp/services/soundproofing.html', context)


def furniture(request):
    """Furniture Assembly Constract"""
    return render(request, 'webapp/services/furniture_assembly.html')


def painting(request):
    """ Painting Constract"""
    disp_obj = DisposalService.objects.all()
    main_serv = Services.objects.all()

    context = locals()
    return render(request, 'webapp/services/painting.html', context)


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

    return render(request, 'webapp/forms/register_form.html', {'form': form})



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
#     return render(request, 'webapp/forms/register_form.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()
            user_profile = form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            login(request, user)
            return redirect('home')  # Замените 'home' на URL вашей главной страницы
    else:
        form = RegistrationForm()
    return render(request, 'webapp/forms/register_form.html', {'form': form})

def error(request):
    """Error page Constract """
    return render(request, 'webapp/error.html')

def events(request):
    """Events page Constract """
    return render(request, 'webapp/event.html')

def checkout(request):
    """Checkout page Constract """
    return render(request, 'webapp/checkout.html')
