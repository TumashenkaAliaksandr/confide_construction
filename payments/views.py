import json
import re

from django.shortcuts import redirect
from django.urls import reverse

from webapp.models import *
from blog.models import *
from django.conf import settings
from django.http.response import JsonResponse,  HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import stripe


from django.views.generic import TemplateView
from django.shortcuts import redirect
from webapp.models import *


class HomePageView(TemplateView):
    template_name = 'payment_stripe.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_serv'] = Services.objects.all()
        context['news'] = BlogNews.objects.all()


        # Получаем ID продукта из GET-запроса
        product_id = self.request.GET.get('product_id')
        print(f"32 string | Product ID from GET request: {product_id}")  # Отладочный вывод

        if product_id:
            try:
                product = Product.objects.get(id=product_id)  # Получаем конкретный продукт по ID
                print(f"37 string | Product found: {product.name}")  # Отладочный вывод

                # Проверяем цену и скидку продукта
                if product.price is not None:
                    context['price'] = float(product.price)  # Преобразуем Decimal в float
                    print(f"42 string | Price This found: {context['price']}")
                else:
                    context['price'] = 0.00  # Устанавливаем значение по умолчанию
                    print("Product price is None, setting to default 0.00")

                if product.discount is not None:
                    context['discount'] = float(product.discount)  # Преобразуем Decimal в float
                    print(f"49 string | Discount found: {context['discount']}")
                else:
                    context['discount'] = 0.00  # Устанавливаем значение по умолчанию
                    print("Product discount is None, setting to default 0.00")

                context['product_name'] = product.name  # Добавляем имя продукта
                context['product_id'] = product.id  # Добавляем ID продукта в контекст
                print(f"56 string | Product ID: {context['product_id']}")

            except Product.DoesNotExist:
                print("Product does not exist.")  # Отладочный вывод
                return redirect('webapp:order_error')

        # Получаем последние детали заказа по времени создания
        last_checkout_details = CheckoutDetails.objects.order_by(
            '-id').first()  # Используем id для получения последнего заказа
        if last_checkout_details:
            context['checkout_details'] = last_checkout_details  # Добавляем последние детали заказа в контекст
            print(f"67 string | Last checkout details found: {last_checkout_details}")
        else:
            context['checkout_details'] = None  # Если деталей нет, устанавливаем None

        return context

    def post(self, request, *args, **kwargs):
        last_name = request.POST.get('last_name_check')
        description = request.POST.get('order_notes')
        street_address = request.POST.get('street_address')
        town_city = request.POST.get('town_city')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        date_check = request.POST.get('date')
        discount_price = request.POST.get('discount_check')
        name_product = request.POST.get('name_check')
        id_product = request.POST.get('product_object_id')

        print(
            f"83 string | Received data: {last_name}, {street_address}, {town_city}, {phone_number}, {email}, {description}, {date_check}, "
            f"{discount_price} {name_product} {id_product}")

        # Получаем ID продукта из формы
        product_id = request.POST.get('product_object_id')  # Получаем ID выбранного продукта
        print(f"90 string | Product ID from POST request: {product_id}")  # Отладочное сообщение

        if product_id:
            try:
                product_id = int(product_id)  # Преобразуем в целое число
            except ValueError:
                return JsonResponse({'error': 'Invalid Product ID'}, status=400)

            # Получаем конкретный продукт по ID
            product = Product.objects.filter(id=product_id).first()
            product_content_type = ContentType.objects.get_for_model(Product)

            if product:
                price = float(product.price) if product.price is not None else 0.00  # Используем цену продукта
                discount = float(
                    product.discount) if product.discount is not None else 0.00  # Используем скидку продукта

                try:
                    checkout_details = CheckoutDetails.objects.create(
                        last_name_check=last_name,
                        order_notes=description,
                        street_address=street_address,
                        town_city=town_city,
                        phone_number=phone_number,
                        email=email,
                        date=date_check,
                        price_check=round(price, 2),  # Округляем до двух знаков после запятой
                        discount_check=round(discount, 2),  # Округляем до двух знаков после запятой
                        name_check=product.name,  # Сохраняем имя продукта
                        product_object_id=product.id,  # Сохраняем ID продукта
                        product_content_type=product_content_type,
                    )
                    print("118 string | CheckoutDetails object created successfully:", checkout_details.product_content_type.id, checkout_details.product)

                    # Перенаправление на payments с параметром product_id
                    return HttpResponseRedirect(f"{reverse('payments')}?product_id={product_id}")

                except Exception as e:
                    print(f"Error creating CheckoutDetails: {e}")
                    return redirect('webapp:error')

            else:
                print("Product not found.")
                return redirect('webapp:order_error')  # Если продукт не найден

        return redirect('webapp:order_error')  # Если метод не POST, перенаправляем обратно


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'GET':
#         domain_url = 'https://dchomefix.co/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:
#             # Получаем последний объект Disposal из базы данных
#             disposal = Disposal.objects.last()
#             if disposal:
#                 # Очищаем значение discount от ненужных символов и преобразуем его в число
#                 discount_cleaned = re.sub(r'[^\d.]', '', str(disposal.discount))
#                 try:
#                     price = int(float(discount_cleaned) * 100)
#                 except ValueError:
#                     return JsonResponse({'error': 'Invalid discount value'})
#
#                 name = disposal.name
#                 descriptions = disposal.description
#
#                 # Создаем новую сессию оформления заказа для товара
#                 checkout_session = stripe.checkout.Session.create(
#                     success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                     cancel_url=domain_url + 'payments/',
#                     payment_method_types=['card'],
#                     mode='payment',
#                     line_items=[
#                         {
#                             'price_data': {
#                                 'currency': 'usd',
#                                 'unit_amount': price,
#                                 'product_data': {
#                                     'name': name,
#                                     'description': descriptions,
#                                 },
#                             },
#                             'quantity': 1,
#                         }
#                     ]
#                 )
#                 return JsonResponse({'sessionId': checkout_session['id']})
#             else:
#                 return JsonResponse({'error': 'No Disposal objects found'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        # domain_url = 'https://dchomefix.co/'
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Получаем ID продукта из GET-запроса
        product_id = request.GET.get('product_id')
        print(f"198 string | Product ID from GET request: {product_id}")  # Отладочный вывод

        if product_id:
            try:
                # Получаем продукт по ID
                product = Product.objects.get(id=product_id)
                print(f"199 string | Product found: {product.name}")  # Отладочный вывод

                # Очищаем значение discount от ненужных символов и преобразуем его в число
                discount_cleaned = re.sub(r'[^\d.]', '', str(product.discount))
                try:
                    price = int(float(discount_cleaned) * 100)  # Преобразуем в центы
                except ValueError:
                    return JsonResponse({'error': 'Invalid discount value'})

                name = product.name
                descriptions = product.description

                # Создаем новую сессию оформления заказа для товара
                checkout_session = stripe.checkout.Session.create(
                    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url=domain_url + f'payments/?product_id={product_id}',
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
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found'})
            except Exception as e:
                return JsonResponse({'error': str(e)})

        return JsonResponse({'error': 'Product ID is required'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'GET':
#         domain_url = 'http://127.0.0.1:8000/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:
#             # Получаем последний объект Product из базы данных
#             product = Product.objects.first()
#             if product:
#                 # Очищаем значение discount от ненужных символов и преобразуем его в число
#                 product_cleaned = re.sub(r'[^\d.]', '', str(product.discount))
#                 try:
#                     price = int(float(product_cleaned) * 100)
#                 except ValueError:
#                     return JsonResponse({'error': 'Invalid discount value'})
#
#                 name = product.name
#                 descriptions = product.description
#
#                 # Создаем новую сессию оформления заказа для товара
#                 checkout_session = stripe.checkout.Session.create(
#                     success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                     cancel_url=domain_url + 'payments/',
#                     payment_method_types=['card'],
#                     mode='payment',
#                     line_items=[
#                         {
#                             'price_data': {
#                                 'currency': 'usd',
#                                 'unit_amount': price,
#                                 'product_data': {
#                                     'name': name,
#                                     'description': descriptions,
#                                 },
#                             },
#                             'quantity': 1,
#                         }
#                     ]
#                 )
#                 return JsonResponse({'sessionId': checkout_session['id']})
#             else:
#                 return JsonResponse({'error': 'No Products objects found'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})


# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'POST':  # Убедитесь, что метод POST используется
#         print("Received request to create checkout session.")  # Отладочное сообщение
#         domain_url = 'http://127.0.0.1:8000/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#
#         try:
#             # Получаем ID продукта из POST-запроса
#             data = json.loads(request.body)
#             print(f"Request body: {data}")  # Отладочное сообщение для тела запроса
#
#             product_id = data.get('product_id')  # Получаем ID продукта из JSON-данных
#             if not product_id:
#                 return JsonResponse({'error': 'Product ID is required'})
#
#             # Получаем объект Product по ID
#             product = Product.objects.filter(pk=product_id).first()
#             if not product:
#                 return JsonResponse({'error': 'Product not found'})
#
#             print(f"Found product: {product.name}")  # Отладочное сообщение для найденного продукта
#
#             # Очищаем значение discount от ненужных символов и преобразуем его в число
#             discount_cleaned = re.sub(r'[^\d.]', '', str(product.discount))
#             try:
#                 price = int(float(discount_cleaned) * 100)  # Преобразуем в центы
#                 print(f"Price in cents: {price}")  # Отладочное сообщение для цены
#             except ValueError:
#                 return JsonResponse({'error': 'Invalid discount value'})
#
#             name = product.name
#             descriptions = product.description
#
#             # Создаем новую сессию оформления заказа для товара
#             checkout_session = stripe.checkout.Session.create(
#                 success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=domain_url + 'payments/',
#                 payment_method_types=['card'],
#                 mode='payment',
#                 line_items=[
#                     {
#                         'price_data': {
#                             'currency': 'usd',
#                             'unit_amount': price,
#                             'product_data': {
#                                 'name': name,
#                                 'description': descriptions,
#                             },
#                         },
#                         'quantity': 1,
#                     }
#                 ]
#             )
#             print("Checkout session created successfully.")  # Отладочное сообщение для успешного создания сессии
#             return JsonResponse({'sessionId': checkout_session['id']})
#         except Exception as e:
#             print(f"Error occurred: {str(e)}")  # Отладочное сообщение для ошибки
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
