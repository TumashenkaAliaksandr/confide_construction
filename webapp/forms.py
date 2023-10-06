from django import forms
from .models import Payment  # Замените .models на путь к вашим моделям

class CallbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'order',
            'payment_amount',
            'payment_method',
            'expiration_date_month',
            'expiration_date_year',
            'cvv',
            'card_number',
            'owner',
            'total_amount',
        ]

