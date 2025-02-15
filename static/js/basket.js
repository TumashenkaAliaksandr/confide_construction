function addToBasket(productId) {
    fetch(`/add_to_basket/${productId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Product has been added to your shopping cart!");
            document.getElementById("cart-count").innerText = data.total_quantity; // Обновляем кружок
            updateBasketTotal();
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}



// Получение CSRF-токена из cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateBasketTotal() {
    fetch("/basket_detail/", {
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        },
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("cart-total").innerText = data.total_price; // Обновляем сумму
        document.getElementById("cart-count").innerText = data.total_items; // Обновляем кружок с количеством товаров
    })
    .catch(error => console.error("Cart update error:", error));
}

