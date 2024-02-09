document.addEventListener('DOMContentLoaded', function () {
  var stripe = Stripe('{{ STRIPE_PUBLISHABLE_KEY }}');

  document.getElementById('checkout-form').addEventListener('submit', function(event) {
    // Отменяем действие по умолчанию (отправку формы)
    event.preventDefault();

    // Создаем сессию оплаты через Stripe Checkout
    stripe.redirectToCheckout({
      lineItems: [{price: '{{ PRICE_ID }}', quantity: 1}],
      mode: 'payment',
      successUrl: 'http://example.com/success/',
      cancelUrl: 'http://example.com/cancel/',
    }).then(function(result) {
      // Обработка ошибок, если таковые возникнут
      if (result.error) {
        // Выводим ошибку на странице
        alert(result.error.message);
      }
    });
  });
});
