from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render


class CallbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutDetails
        fields = ['first_name', 'last_name', 'company_name', 'street_address', 'town_city', 'phone_number', 'email', 'order_notes', 'user']



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


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your name'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Your email'}
        )
    )

    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'cols': 30, 'rows': 5}
        )
    )


def contact(request):
    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка отправки формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка письма
            send_mail(
                'Feedback from your website',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'tumashenkaaliaksandr@gmail.com',  # Отправитель
                ['recipient@example.com'],  # Получатель
                fail_silently=False,
            )

            return HttpResponseRedirect('')  # Перенаправление на страницу "Спасибо"
    else:
        form = ContactForm()

    context['form'] = form
    return render(request, 'webapp/contact-us-1.html', context=context)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = User_Photo
        fields = ['image']
