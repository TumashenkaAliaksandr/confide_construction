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

        # Получаем последний объект Disposal и добавляем его дисконт в контекст
        disposal = Disposal.objects.last()  # Или используйте другой способ получения объекта
        if disposal:
            context['discount'] = disposal.discount  # Добавляем дисконт в контекст
            context['price'] = disposal.price  # Если нужно, добавьте и цену

        context['checkout_details'] = CheckoutDetails.objects.last()
        return context

    def post(self, request, *args, **kwargs):
        last_name = request.POST.get('last_name_check')
        first_name = request.POST.get('first_name_check')
        description = request.POST.get('order_notes')
        street_address = request.POST.get('street_address')
        town_city = request.POST.get('town_city')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        date_check = request.POST.get('date')

        # Получаем последний объект Disposal
        disposal = Disposal.objects.last()  # Или используйте другой способ получения объекта

        # Проверяем, существует ли объект Disposal
        if disposal:
            price = disposal.discount.quantize(Decimal('1.00'))  # Используем дисконт из объекта Disposal
        else:
            price = 0  # Установите значение по умолчанию, если объект не найден

        # Выводим полученные значения для отладки
        print("Received data from the form:")
        print("Last Name:", last_name)
        print("First Name:", first_name)
        print("Price:", price)
        print("Descriptions:", description)
        print("Street Address:", street_address)
        print("Town City:", town_city)
        print("Phone Number:", phone_number)
        print("Email:", email)
        print("Date Check:", date_check)

        # Создайте объект CheckoutDetails и сохраните его в базу данных
        checkout_details = CheckoutDetails.objects.create(
            last_name_check=last_name,
            first_name_check=first_name,
            # discount=price,  # Сохраняем дисконт как цену
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
            # Получаем последний объект Disposal из базы данных
            disposal = Disposal.objects.last()
            if disposal:
                # Очищаем значение discount от ненужных символов и преобразуем его в число
                discount_cleaned = re.sub(r'[^\d.]', '', str(disposal.discount))
                try:
                    price = int(float(discount_cleaned) * 100)
                except ValueError:
                    return JsonResponse({'error': 'Invalid discount value'})

                name = disposal.name
                descriptions = disposal.description

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
                return JsonResponse({'error': 'No Disposal objects found'})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
