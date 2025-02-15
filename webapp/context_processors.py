from .models import Basket, BasketItem

def basket_context(request):
    basket_items = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
        if basket:
            basket_items = BasketItem.objects.filter(basket=basket)
    return {'basket_items': basket_items}
