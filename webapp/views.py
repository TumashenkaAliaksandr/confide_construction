from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView
# from stripe.api_resources.product import Product
from django.shortcuts import get_object_or_404

from blog.models import BlogNews
from webapp.models import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .forms import CheckoutForm
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.db import IntegrityError
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from .models import CheckoutDetails
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from payments.views import create_checkout_session


def index(request):
    """Main, index constr"""
    serv = Services.objects.all()
    people = Review.objects.all()
    partner = Recommended.objects.all()
    project_constract = Project.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()
    news = BlogNews.objects.all()
    product = Product.objects.all()
    products_with_flag_1 = Product.objects.filter(flag_1=True)

    context = locals()
    return render(request, 'webapp/index-2.html', context)


def services(request):
    """Services Constract"""
    serv_serv = Services.objects.all()
    qual = Quality.objects.all()
    servis_slider = ServicesSlider.objects.all()
    main_ser = Services.objects.filter(is_main=True).first()
    sl_serv = Services.objects.all()
    news = BlogNews.objects.all()
    product = Product.objects.all()

    context = locals()
    return render(request, 'webapp/services/services.html', context)


def shop(request):
    """Shop Constract"""
    services_shop = Services.objects.all()
    news = BlogNews.objects.all()
    partner = Recommended.objects.all()

    context = locals()
    return render(request, 'webapp/shop/shop.html', context=context)


def lost_password(request):
    """Lost Password Confide Constraction"""
    news = BlogNews.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'webapp/register/lost_password.html', context=context)


def about(request):
    assessment = Assessment.objects.all()
    partner = Recommended.objects.all()
    servis_sliders = Product.objects.all()
    news = BlogNews.objects.all()

    context = {
        'assessment': assessment,
        'partner': partner,
        'servis_sliders': servis_sliders,
        'news': news,
    }
    return render(request, 'webapp/about-us.html', context=context)


def contacts(request):
    news = BlogNews.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        if email and description:
            send_mail(
                subject='Message from your website',
                message=f'Name: {name}\nEmail: {email}\nMessage: {description}',
                from_email='tumashenkaaliaksandr@gmail.com',
                recipient_list=['Badminton500@inbox.lv'],  # Замените на ваш адрес получателя
                fail_silently=False,
            )

            return render(request, 'webapp/register/success.html')  # Шаблон для страницы успешной отправки
    context = {
        'news': news,
    }
    return render(request, 'webapp/contact-us-1.html', context=context)  # Шаблон с формой обратной связи


def backsplash(request):
    """Backsplash Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/backsplash.html', context=context)


def drywall(request):
    """Drywall Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/drywall.html', context)


def disposal(request):
    """Disposal Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()
    assessment = Assessment.objects.all()

    # Создаем чекаут-сессию
    checkout_session = checkout(request)

    context = locals()
    return render(request, 'webapp/services/disposal.html', context)


def ceiling_fan(request):
    """Disposal Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()
    assessment = Assessment.objects.all()

    # Создаем чекаут-сессию
    checkout_session = checkout(request)

    context = locals()
    return render(request, 'webapp/services/cailing_fan.html', context)


def electricalworks(request):
    """Electricalworks Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/electricalworks.html', context=context)


def handyman(request):
    """Handyman Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/handyman.html', context=context)


def tv_mount(request):
    """Tv Mount Constract"""

    tv_obj = Product.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()
    assessment = Assessment.objects.all()

    # Создаем чекаут-сессию
    checkout_session = create_checkout_session(request)

    context = locals()
    return render(request, 'webapp/services/tv_mount.html', context)


def wallpaper(request):
    """Wallpaper Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()

    return render(request, 'webapp/services/wallpaper.html', context=context)


def soundproofing(request):
    """Soundproofing Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/soundproofing.html', context)


def furniture(request):
    """Furniture Assembly Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()

    return render(request, 'webapp/services/furniture_assembly.html', context=context)


def painting(request):
    """ Painting Constract"""
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/painting.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            user_profile = Profile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']  # Храните пароли в зашифрованном виде
            )

            # Аутентификация пользователя
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)

            return redirect('webapp:home')
    else:
        form = RegistrationForm()
    return render(request, 'webapp/forms/register_form.html', {'form': form})


class CRloginView(LoginView):
    template_name = 'webapp/register/login.html'
    news = BlogNews.objects.all()
    redirect_authenticated_user = True


def logout(request):
    auth_logout(request)
    news = BlogNews.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'webapp/register/logout.html', context=context)


@csrf_protect
def login_view(request):
    news = BlogNews.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Вход выполнен успешно, перенаправляем пользователя на нужную страницу
            return HttpResponseRedirect('home')  # Например, на главную страницу

    context = {
        'news': news,
    }
    return render(request, 'webapp/register/login.html', context=context)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'webapp/register/my_account.html'
    context_object_name = 'page_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowFormsProfilePageView(DetailView):
    model = CheckoutDetails
    template_name = 'webapp/register/my_account.html'
    context_object_name = 'page_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def my_view(request):
    profile = request.user.profile  # Получение профиля пользователя
    advertisement = Advertisement.objects.all()
    return render(request, 'webapp/register/my_account.html', {'profile': profile, 'advertisement': advertisement})


class UpdateProfilePageView(UpdateView):
    model = Profile
    news = BlogNews.objects.all()

    template_name = 'webapp/register/create_profile.html'
    fields = ['first_name', 'last_name', 'phone', 'email', 'password', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('webapp:my_account')


@login_required(login_url='/login/')
def my_account(request):
    news = BlogNews.objects.all()
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    photos = User_Photo.objects.filter(user_profile=profile)  # Используйте поле user_profile
    checkout_details = CheckoutDetails.objects.last()

    context = {
        'news': news,
        'photos': photos,
        'profile': profile,
        'checkout_details': checkout_details,
    }

    return render(request, 'webapp/register/my_account.html', context=context)


def registerdone(request):
    return render(request, 'webapp/register/register_done.html')


def error(request):
    """Error page Constract """
    return render(request, 'webapp/error.html')


# @login_required(login_url='/login/')
# def checkout(request):
#     """Checkout page Construct"""
#
#     news = BlogNews.objects.all()
#     main_serv = Services.objects.all()
#     partner = Recommended.objects.all()
#     checkout_details = CheckoutDetails.objects.last()  # Получаем последний объект CheckoutDetails
#     checkout_disposal = Disposal.objects.last()  # Получаем последний объект CheckoutDetails
#     checkout_session = create_checkout_session(request)
#     discount = checkout_disposal.discount if checkout_disposal else None
#
#     context = {
#         'news': news,
#         'main_serv': main_serv,
#         'partner': partner,
#         'checkout_details': checkout_details,
#         'checkout_disposal': checkout_disposal,
#         'checkout_session': checkout_session,
#         'discount': discount,  # Добавляем дисконт в контекст
#     }
#     return render(request, '../templates/webapp/shop/checkout.html', context=context)


def checkout(request):
    """Checkout page Construct"""

    # Общие данные
    news = BlogNews.objects.all()
    main_serv = Services.objects.all()
    partner = Recommended.objects.all()
    slider_product = Product.objects.all()

    # Получаем ID продукта из GET-запроса
    product_id = request.GET.get('product_id')
    print('498 string | product id:', product_id)
    if not product_id:
        # Если нет ID продукта, перенаправляем на страницу ошибки
        return redirect('webapp:order_error')

    try:
        # Получаем продукт по ID
        product = Product.objects.get(id=product_id)
        print('406 string | More product id:', product_id)
    except Product.DoesNotExist:
        # Если продукт не найден, перенаправляем на страницу ошибки
        return redirect('webapp:order_error')

    # Создаем экземпляр формы, передавая данные о продукте
    form = CheckoutForm(product=product)

    # Формируем контекст для передачи в шаблон
    context = {
        'news': news,
        'main_serv': main_serv,
        'product': product,
        'slider_product': slider_product,
        'form': form,  # Передаем форму
        'discount_check': product.discount,
        'price': product.price,
        'partner': partner,
    }

    # Рендерим страницу чекаута
    return render(request, 'webapp/shop/checkout.html', context=context)


stripe.api_key = settings.STRIPE_SECRET_KEY


# @login_required(login_url='/login/')
# def process_payment(request):
#     news = BlogNews.objects.all()
#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             try:
#                 # Получаем объект Disposal (например, первый объект или по какому-то критерию)
#                 disposal = Disposal.objects.first()  # Замените на нужный вам запрос
#
#                 # Проверяем, существует ли объект Disposal
#                 if not disposal:
#                     return redirect('webapp:order_error')
#
#                 # Сохраняем данные заказа
#                 checkout_details = CheckoutDetails.objects.create(
#                     first_name=form.cleaned_data['first_name'],
#                     last_name=form.cleaned_data['last_name'],
#                     street_address=form.cleaned_data['street_address'],
#                     town_city=form.cleaned_data['town_city'],
#                     phone_number=form.cleaned_data['phone_number'],
#                     email=form.cleaned_data['email'],
#                     order_notes=form.cleaned_data['order_notes'],
#                     date=form.cleaned_data['date'],
#                     price_check=str(disposal.discount),  # Используем цену из модели Disposal
#                 )
#                 # Перенаправляем на страницу с обзором заказа
#                 return redirect('payments', checkout_id=checkout_details.pk)
#             except IntegrityError as e:
#                 # Обработка ошибок при сохранении в базе данных
#                 return redirect('webapp:order_error')
#     else:
#         form = CheckoutForm()
#         checkout_details = None
#
#     context = {
#         'news': news,
#         'form': form,
#         'checkout_details': checkout_details,
#     }
#
#     return render(request, 'webapp/shop/cart.html', context)

def process_payment(request):
    if request.method == 'POST':
        print("Received POST request")  # Отладочное сообщение
        # Получаем данные из формы
        form = CheckoutForm(request.POST)

        if form.is_valid():
            # Получаем данные из формы
            last_name = request.POST.get('last_name_check')
            description = request.POST.get('order_notes')
            street_address = request.POST.get('street_address')
            town_city = request.POST.get('town_city')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            date_check = request.POST.get('date')
            product_id = request.POST.get('product_object_id')
            session_id = request.POST.get('session_id')  # Получаем ID сессии


            # Выводим все данные в консоль
            print(f"Last Name: {last_name}")
            print(f"Order Notes: {description}")
            print(f"Street Address: {street_address}")
            print(f"Town/City: {town_city}")
            print(f"Phone Number: {phone_number}")
            print(f"Email: {email}")
            print(f"Date: {date_check}")
            print(f"Product ID: {product_id}")
            print(f"Session ID: {session_id}")

            # Получаем конкретный продукт по ID
            try:
                product = Product.objects.get(id=product_id)
                print(f"Product found: {product.name}")  # Отладочный вывод
                price = form.cleaned_data.get('price_check', 0.00)  # Значение по умолчанию
                discount = form.cleaned_data.get('discount_check', 0.00)  # Значение по умолчанию

                print(f"Price from form: {price}")
                print(f"Discount from form: {discount}")

                # Получаем ContentType для продукта
                product_content_type = ContentType.objects.get_for_model(Product)

                try:
                    checkout_details = CheckoutDetails.objects.create(
                        last_name_check=last_name,
                        order_notes=description,
                        street_address=street_address,
                        town_city=town_city,
                        phone_number=phone_number,
                        email=email,
                        date=date_check,
                        price_check=product.price,
                        discount_check=product.discount,
                        name_check=product.name,
                        product_content_type=product_content_type,
                        product_object_id=product.id
                    )
                    print("CheckoutDetails object This created successfully:", checkout_details)

                    # Выводим все атрибуты объекта checkout_details
                    print("CheckoutDetails attributes:")
                    print(f"Last Name: {checkout_details.last_name_check}")
                    print(f"Order Notes: {checkout_details.order_notes}")
                    print(f"Street Address: {checkout_details.street_address}")
                    print(f"Town/City: {checkout_details.town_city}")
                    print(f"Phone Number: {checkout_details.phone_number}")
                    print(f"Email: {checkout_details.email}")
                    print(f"Date: {checkout_details.date}")
                    print(f"Price: {checkout_details.price_check}")
                    print(f"Discount: {checkout_details.discount_check}")

                    # Сохраняем данные сессии в базе данных
                    checkout_session = CheckoutSession.objects.create(
                        # session_id=session_id,
                        product=product,
                        user_email=email,
                        last_name_check=last_name,
                        street_address=street_address,
                        town_city=town_city,
                        phone_number=phone_number,
                        order_notes=description,
                        date=date_check,
                        price_check=product.price,
                        discount_check=product.discount
                    )
                    print("CheckoutSession object created successfully:", checkout_session)

                    # Выводим все атрибуты объекта checkout_session
                    print("CheckoutSession attributes:")
                    print(f"Session ID: {checkout_session.session_id}")
                    print(f"Product: {checkout_session.product.name}")  # Предполагается, что у продукта есть атрибут name
                    print(f"User Email: {checkout_session.user_email}")

                    # Отладочный принт о том, что данные записались
                    print("Data saved successfully for CheckoutDetails and CheckoutSession.")

                    return JsonResponse({'success': True})  # Возвращаем успешный ответ в формате JSON

                except Exception as e:
                    print(f"Error creating CheckoutDetails or CheckoutSession: {e}")
                    return JsonResponse({'success': False, 'error': str(e)}, status=400)

            except Product.DoesNotExist:
                print("Product not found.")
                return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)  # Если продукт не найден

        print("Request method is not POST.")
        return redirect('webapp:checkout')  # Если метод не POST, перенаправляем обратно


def order_exists(request):
    """errors payment"""
    news = BlogNews.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'webapp/shop/order_error.html', context=context)


def order_error(request):
    """errors payment"""
    news = BlogNews.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'webapp/shop/order_error.html', context=context)


def base(request, slug):
    """Base page Constract """
    # news = BlogNews.objects.filter(pk=pk)
    news_blog_main = BlogNews.objects.all()
    products = Product.objects.all()
    product = get_object_or_404(Product, slug=slug)

    context = {
        # 'news': news,
        'news_blog_main': news_blog_main,
        'products': products,
        'product': product,
    }

    return render(request, 'main/base.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # Получаем продукт по ID

    context = {
        'product': product,
    }

    return render(request, 'webapp/services/product_detail.html', context)


class Search(ListView):
    template_name = 'blog/blog-details.html'
    context_object_name = 'news'  # Исправлено имя контекста

    def get_queryset(self):
        search_query = self.request.GET.get('s', '')
        if search_query:
            return BlogNews.objects.filter(title__icontains=search_query)
        return BlogNews.objects.none()  # Пустой queryset, если нет запроса

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')  # Передача поискового запроса в контекст
        return context


def comingsoon(request):
    """Comingsoon page Constract """
    return render(request, 'webapp/comingsoon.html')


def success(request):
    """Success page Constract """
    return render(request, 'webapp/register/success.html')


def single_product(request, slug):
    """Single product page Construct"""
    product = get_object_or_404(Product, slug=slug)
    product_name = Product.objects.all()
    checkout_session = checkout(request)  # Предположим, что функция checkout возвращает сессию

    context = {
        'product': product,
        'product_name': product_name,
        'checkout_session': checkout_session,
        'current_name': request.user.first_name if request.user.is_authenticated else '',  # Пример получения имени
    }
    return render(request, 'webapp/shop/single_product.html', context=context)

