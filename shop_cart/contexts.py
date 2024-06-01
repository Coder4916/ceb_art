from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for artwork_id, artwork_data in cart.items():
        if isinstance(artwork_data, int):
            product = get_object_or_404(Product, pk=artwork_id)
            total += artwork_data * product.price
            product_count += artwork_data
            cart_items.append({
                'artwork_id': artwork_id,
                'quantity': artwork_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=artwork_id)
            for size, quantity in artwork_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                'artwork_id': artwork_id,
                'quantity': quantity,
                'product': product,
                'size': size,
            })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
