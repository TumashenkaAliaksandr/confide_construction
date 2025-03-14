from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.validators import RegexValidator
from django.core.files.storage import FileSystemStorage
from multiupload.fields import MultiFileField

class CallbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)


# class CheckoutForm(forms.ModelForm):
#     date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'lang': 'en-us'}))
#
#     # Валидатор для поля price_check
#     price_check = forms.CharField(max_length=100, validators=[RegexValidator(
#         r'^\d+(\.\d{1,2})?$', 'Введите корректное числовое значение'
#     )])
#
#     # Поля из модели Disposal
#     discount = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
#     price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
#
#     class Meta:
#         model = CheckoutDetails
#         fields = [
#             # 'first_name_check',
#             'last_name_check',
#             'street_address',
#             'town_city',
#             'phone_number',
#             'date',
#             'email',
#             'order_notes',
#             'price_check',
#             'discount',
#             'price'
#         ]
#
#     def __init__(self, *args, **kwargs):
#         # Получаем объект Disposal, если он передан
#         self.disposal = kwargs.pop('disposal', None)
#         super().__init__(*args, **kwargs)
#
#         # Если объект Disposal передан, устанавливаем значения полей discount и price
#         if self.disposal:
#             self.fields['discount'].initial = self.disposal.discount
#             self.fields['price'].initial = self.disposal.price


class CheckoutForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'lang': 'en-us'}))

    discount_check = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    price_check = forms.DecimalField(widget=forms.HiddenInput(), required=False)
    name_check = forms.CharField(widget=forms.HiddenInput(), required=False)

    product_content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.all(),
        widget=forms.HiddenInput()
    )
    product_object_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = CheckoutDetails
        fields = [
            'last_name_check',
            'street_address',
            'town_city',
            'phone_number',
            'date',
            'email',
            'order_notes',
            'discount_check',
            'price_check',
            'name_check',
            'product_content_type',
            'product_object_id',
        ]

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)

        if product:
            self.fields['discount_check'].initial = product.discount
            self.fields['price_check'].initial = product.price
            self.fields['name_check'].initial = product.name


            # Отладочные сообщения для проверки значений
            print(f"Initializing CheckoutForm with product: {product.name}")
            print(f"Discount set to: {self.fields['discount_check'].initial}")
            print(f"Price set to: {self.fields['price_check'].initial}")
            print(f"Name set to: {self.fields['name_check'].initial}")
    print('Id:', product_object_id)


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)  # Встроенная проверка пароля Django
        return password


# class ContactForm(forms.Form):
#     name = forms.CharField(
#         min_length=2,
#         widget=forms.TextInput(
#             attrs={'placeholder': 'Your name'}
#         )
#     )
#
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={'placeholder': 'Your email'}
#         )
#     )
#
#     message = forms.CharField(
#         min_length=20,
#         widget=forms.Textarea(
#             attrs={'placeholder': 'Message', 'cols': 30, 'rows': 5}
#         )
#     )

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class ContactForm(forms.Form):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'mailpoet_text'}),
        label="First Name"
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'mailpoet_text'}),
        label="Last Name"
    )

    zip_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'ZIP Code', 'class': 'mailpoet_text'}),
        label="ZIP Code"
    )

    description = forms.CharField(
        min_length=5,
        widget=forms.Textarea(attrs={'placeholder': 'Please describe the job in detail.', 'class': 'mailpoet_text'}),
        label="Job Description"
    )

    hours = forms.ChoiceField(
        choices=[(str(i), f"{i} Hour{'s' if i > 1 else ''}") for i in range(1, 10)],
        widget=forms.Select(attrs={'class': 'mailpoet_text'}),
        label="How many hours would you like to book?"
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'mailpoet_text'}),
        label="When would you like a Pro to come?"
    )

    time = forms.ChoiceField(
        choices=[(f"{i}:00 AM", f"{i}:00 AM") for i in range(1, 13)] +
                [(f"{i}:30 AM", f"{i}:30 AM") for i in range(1, 13)] +
                [(f"{i}:00 PM", f"{i}:00 PM") for i in range(1, 13)] +
                [(f"{i}:30 PM", f"{i}:30 PM") for i in range(1, 13)],
        widget=forms.Select(attrs={'class': 'mailpoet_text'}),
        label="At what time?"
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'mailpoet_text'}),
        label="Email Address"
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number (e.g. 123-456-7890)', 'class': 'mailpoet_text'}),
        label="Phone Number"
    )

    # Используем кастомное поле для загрузки нескольких фото
    photos = MultipleFileField(
        required=False,
        widget=MultipleFileInput(attrs={'class': 'mailpoet_text'}),
        label="Photo"
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'zip_code',
            'job_description', 'hours_needed',
            'appointment_date', 'appointment_time',
            'email', 'phone', 'photo'
        ]
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

# def contact(request):
#     context = {}
#
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Обработка отправки формы
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#
#             # Отправка письма
#             send_mail(
#                 'Feedback from your website',
#                 f'Name: {name}\nEmail: {email}\nMessage: {message}',
#                 'tumashenkaaliaksandr@gmail.com',  # Отправитель
#                 ['Badminton500@inbox.lv'],  # Получатель
#                 fail_silently=False,
#             )
#
#             return HttpResponseRedirect('')  # Перенаправление на страницу "Спасибо"
#     else:
#         form = ContactForm()
#
#     context['form'] = form
#     return render(request, 'webapp/contact-us-1.html', context=context)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = User_Photo
        fields = ['image']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client_name', 'client_email', 'amount', 'description', 'invoice_link']
        widgets = {
            'invoice_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter invoice link'}),
        }


class BasketItemForm(forms.ModelForm):
    class Meta:
        model = BasketItem
        fields = ['product', 'quantity']

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['user']  # В корзине может быть только один пользователь
