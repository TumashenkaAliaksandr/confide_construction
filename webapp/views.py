from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView
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



def index(request):
    """Main, index constr"""
    serv = Services.objects.all()
    people = Review.objects.all()
    partner = Recommended.objects.all()
    project_constract = Project.objects.all()
    main_serv = Services.objects.filter(is_main=True).first()
    news = BlogNews.objects.all()

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

    context = locals()
    return render(request, 'webapp/services.html', context)


def shop(request):
    """Shop Constract"""
    services_shop = Services.objects.all()
    news = BlogNews.objects.all()
    partner = Recommended.objects.all()

    context = locals()
    return render(request, 'webapp/shop.html', context=context)


def lost_password(request):
    """Lost Password Confide Constraction"""
    news = BlogNews.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'webapp/lost_password.html', context=context)


def about(request):
    assessment = Assessment.objects.all()
    partner = Recommended.objects.all()
    servis_sliders = ServicesSlider.objects.all()
    news = BlogNews.objects.all()

    context = {
        'assessment': assessment,
        'partner': partner,
        'servis_sliders': servis_sliders,
        'news': news,
    }
    return render(request, 'webapp/about-us.html', context=context)


def contacts(request):
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

            return render(request, 'webapp/success.html')  # Шаблон для страницы успешной отправки

    return render(request, 'webapp/contact-us-1.html')  # Шаблон с формой обратной связи


def backsplash(request):
    """Backsplash Constract"""
    back_sp = Backsplash.objects.all()
    back_spl_serv = BacksplashService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/backsplash.html', context=context)


def drywall(request):
    """Drywall Constract"""
    dry_obj = Drywall.objects.all()
    dry_ser = DrywallService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/drywall.html', context)


def disposal(request):
    """Disposal Constract"""
    disp_obj = Disposal.objects.all()
    disp_serv = DisposalService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/disposal.html', context)


def electricalworks(request):
    """Electricalworks Constract"""
    electr_obj = Electrical.objects.all()
    electr_serv = ElectricalService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/electricalworks.html', context=context)


def handyman(request):
    """Handyman Constract"""
    handyman_obj = Handyman.objects.all()
    handy_serv = HandymanService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/handyman.html', context=context)


def wallpaper(request):
    """Wallpaper Constract"""

    wallpap_obj = Wallpaper.objects.all()
    wallpap_serv = WallpaperService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()

    return render(request, 'webapp/services/wallpaper.html', context=context)


def soundproofing(request):
    """Soundproofing Constract"""
    soundproof_obj = Soundproofing.objects.all()
    soundproof_serv = SoundproofingService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()
    return render(request, 'webapp/services/soundproofing.html', context)


def furniture(request):
    """Furniture Assembly Constract"""
    furniture_obj = Furniture.objects.all()
    furnitur_serv = FurnitureService.objects.all()
    main_serv = Services.objects.all()
    news = BlogNews.objects.all()

    context = locals()

    return render(request, 'webapp/services/furniture_assembly.html', context=context)


def painting(request):
    """ Painting Constract"""
    painting_obj = Painting.objects.all()
    paint_serv = PaintingService.objects.all()
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
    template_name = 'webapp/login.html'
    news = BlogNews.objects.all()
    redirect_authenticated_user = True


def logout(request):
    auth_logout(request)
    news = BlogNews.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'webapp/logout.html', context=context)


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
    return render(request, 'webapp/login.html', context=context)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'webapp/my_account.html'
    context_object_name = 'page_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def my_view(request):
    profile = request.user.profile  # Получение профиля пользователя
    advertisement = Advertisement.objects.all()
    return render(request, 'webapp/my_account.html', {'profile': profile, 'advertisement': advertisement})


class UpdateProfilePageView(UpdateView):
    model = Profile
    news = BlogNews.objects.all()

    template_name = 'webapp/create_profile.html'
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

    context = {
        'news': news,
        'photos': photos,
        'profile': profile,
    }

    return render(request, 'webapp/my_account.html', context=context)


def registerdone(request):
    return render(request, 'webapp/register_done.html')


def error(request):
    """Error page Constract """
    return render(request, 'webapp/error.html')


@login_required(login_url='/login/')
def checkout(request):
    """Checkout page Construct"""
    news = BlogNews.objects.all()
    main_serv = Services.objects.all()
    partner = Recommended.objects.all()
    checkout_details = CheckoutDetails.objects.filter(user=request.user).first()

    context = {
        'news': news,
        'main_serv': main_serv,
        'partner': partner,
        'checkout_details': checkout_details,
    }
    return render(request, 'webapp/checkout.html', context=context)


@login_required(login_url='/login/')
def process_payment(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout_details = CheckoutDetails.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                street_address=form.cleaned_data['street_address'],
                town_city=form.cleaned_data['town_city'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                order_notes=form.cleaned_data['order_notes'],
                date=form.cleaned_data['date'],
                price=form.cleaned_data['price'],
                user=request.user,  # Предполагается, что у вас есть переменная request с доступом к пользователю
            )
            checkout_details.save()
            return redirect('webapp:success')  # Перенаправление на страницу успешного оформления заказа
    else:
        form = CheckoutForm()

    context = {'form': form}
    return render(request, 'webapp/cart.html', context)


def base(request, pk):
    """Base page Constract """
    news = BlogNews.objects.filter(pk=pk)
    news_blog_main = BlogNews.objects.all()

    context = {
        'news': news,
        'news_blog_main': news_blog_main
    }

    return render(request, 'webapp/blog_footer_info.html', context=context)


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
    return render(request, 'webapp/success.html')