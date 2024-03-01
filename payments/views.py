from webapp.models import *
from blog.models import *
from django.conf import settings
from django.db.models import Sum
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView
import stripe


class HomePageView(TemplateView):
    template_name = 'payment_stripe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_serv'] = Services.objects.all()
        context['news'] = BlogNews.objects.all()
        return context


# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Получаем первый объект Disposal из базы данных
            disposal = Disposal.objects.first()
            if disposal:
                price = int(disposal.price * 100)  # Преобразуем цену в центы
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
                        },
                        {
                            'price_data': {
                                'currency': 'usd',
                                'unit_amount': 15,
                                'product_data': {
                                    'name': 'Dimon',
                                    'description': 'Описание',
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
