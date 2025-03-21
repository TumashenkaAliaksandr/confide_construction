document.addEventListener('DOMContentLoaded', function() {
    const paymentDropdown = document.getElementById('payment-dropdown');
    const paymentDetailsDiv = document.getElementById('payment-details');

    paymentDropdown.addEventListener('change', function() {
        showPaymentDetails(this.value);
    });

    function showPaymentDetails(paymentId) {
        if (!paymentId) {
            paymentDetailsDiv.innerHTML = '';
            return;
        }

        // Поскольку мы не можем напрямую использовать Django шаблонные теги в JS файле,
        // нам нужно передать данные из Django в JavaScript через JSON.
        // Для этого в HTML добавьте скрытый элемент с данными.
        const paymentsDataElement = document.getElementById('payments-data');
        if (!paymentsDataElement) {
            console.error("Element with ID 'payments-data' not found.  Make sure you have it in your HTML.");
            paymentDetailsDiv.innerHTML = '<p>Error: Payments data not found.</p>';
            return;
        }

        const paymentsJson = paymentsDataElement.textContent;
        let payments;

        try {
            payments = JSON.parse(paymentsJson);
        } catch (e) {
            console.error("Error parsing JSON: ", e);
            paymentDetailsDiv.innerHTML = '<p>Error: Could not parse payments data.</p>';
            return;
        }

        const selectedPayment = payments.find(payment => payment.id == paymentId);

        if (selectedPayment) {
            let tableHTML = `
                <table class="payment-detail-table shop_table rt-checkout-review-order-table">
                    <tr><th>Payment ID:</th><td>${selectedPayment.id}</td></tr>
                    <tr><th>Date:</th><td>${selectedPayment.date}</td></tr>
                    <tr><th>Name Check:</th><td>${selectedPayment.name_check}</td></tr>
                    <tr><th>Last Name:</th><td>${selectedPayment.last_name_check}</td></tr>
                    <tr><th>Town City:</th><td>${selectedPayment.town_city}</td></tr>
                    <tr><th>Street Adress:</th><td>${selectedPayment.street_address}</td></tr>
                    <tr><th>Phone Number:</th><td>${selectedPayment.phone_number}</td></tr>
                    <tr><th>Price:</th><td>${selectedPayment.price_check}$</td></tr>
                    <tr><th>Description:</th><td>${selectedPayment.order_notes}</td></tr>
                </table>
            `;

            paymentDetailsDiv.innerHTML = tableHTML;

        } else {
            paymentDetailsDiv.innerHTML = '<p>Payment details not found.</p>';
        }
    }
});
