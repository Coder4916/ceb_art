from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for artwork_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=artwork_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'artwork_id': artwork_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
