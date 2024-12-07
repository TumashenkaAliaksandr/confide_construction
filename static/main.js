// // static/main.js
//
// console.log("Sanity check!");
//
// // Get Stripe publishable key
// fetch("/payments/config/")
// .then((result) => { return result.json(); })
// .then((data) => {
//   // Initialize Stripe.js
//   const stripe = Stripe(data.publicKey);
//
//   // new
//   // Event handler
//   document.querySelector("#submitBtn").addEventListener("click", () => {
//     // Get Checkout Session ID
//     fetch("create-checkout-session/")
//     .then((result) => { return result.json(); })
//     .then((data) => {
//       console.log(data);
//       // Redirect to Stripe Checkout
//       return stripe.redirectToCheckout({sessionId: data.sessionId})
//     })
//     .then((res) => {
//       console.log(res);
//     });
//   });
// });

console.log("Sanity check!");

// Get Stripe publishable key
fetch("/payments/config/")
  .then((result) => { return result.json(); })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);

    // Event handler for the submit button
    document.querySelector("#submitBtn").addEventListener("click", () => {
      // Get the product ID from a hidden input field or from the button's data attribute
      const productId = document.querySelector('input[name="product_object_id"]').value; // Получаем ID продукта из скрытого поля

      // Get Checkout Session ID
      fetch(`/payments/create-checkout-session/?product_id=${productId}`) // Передаем product_id в запросе
        .then((result) => {
          if (!result.ok) {
            throw new Error('Network response was not ok');
          }
          return result.json();
        })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.sessionId });
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    });
  });
