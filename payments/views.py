import re

from webapp.models import *
from blog.models import *
from django.conf import settings
from django.http.response import JsonResponse,  HttpResponseRedirect # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView
import stripe


class HomePageView(TemplateView):
    template_name = 'payment_stripe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_serv'] = Services.objects.all()
        context['news'] = BlogNews.objects.all()
        context['checkout_details'] = CheckoutDetails.objects.last()
        return context

    def post(self, request, *args, **kwargs):
        last_name = request.POST.get('last_name_check')
        first_name = request.POST.get('first_name_check')
        price = request.POST.get('price_check')
        description = request.POST.get('order_notes')
        street_address = request.POST.get('street_address')
        town_city = request.POST.get('town_city')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        date_check = request.POST.get('date')

        # Выводим полученные значения для отладки
        print("Received data from the form:")
        print("Last Name:", last_name)
        print("First Name:", first_name)
        print("Price:", price)
        print("Descriptions:", description)
        print("street_address:", street_address)
        print("Town_City:", town_city)
        print("phone_number:", phone_number)
        print("Email:", email)
        print("Date Check:", date_check)

        # Создайте объект CheckoutDetails и сохраните его в базу данных
        checkout_details = CheckoutDetails.objects.create(
            last_name_check=last_name,
            first_name_check=first_name,
            price_check=price,
            order_notes=description,
            street_address=street_address,
            town_city=town_city,
            phone_number=phone_number,
            email=email,
            date=date_check,
            # Укажите остальные поля объекта CheckoutDetails
        )
        print("CheckoutDetails object created successfully:", checkout_details)

        return HttpResponseRedirect('', checkout_details)



# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Получаем первый объект CheckoutDetails из базы данных
            checkout_details = CheckoutDetails.objects.last()
            if checkout_details:
                # Очищаем значение price_check от ненужных символов и преобразуем его в число
                price_check_cleaned = re.sub(r'[^\d.]', '', checkout_details.price_check)
                try:
                    price = int(float(price_check_cleaned) * 100)
                except ValueError:
                    return JsonResponse({'error': 'Invalid price_check value'})

                name = checkout_details.first_name_check
                descriptions = checkout_details.order_notes

                # Создаем новую сессию оформления заказа для товара
                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url=domain_url + 'payments/',
                    payment_method_types=['card'],
                    mode='payment',
                    line_items=[
                        {
                            'price_data': {
                                'currency': 'usd',
                                'unit_amount': price,
                                'product_data': {
                                    'name': name,
                                    'description': descriptions,
                                },
                            },
                            'quantity': 1,
                        }
                    ]
                )
                return JsonResponse({'sessionId': checkout_session['id']})
            else:
                return JsonResponse({'error': 'No CheckoutDetails objects found'})
        except Exception as e:
            return JsonResponse({'error': str(e)})

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
