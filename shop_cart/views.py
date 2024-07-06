from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view that renders the bag contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.artwork} quantity to '
                                  f'{cart[item_id]["items_by_size"][size]}'))
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.artwork} to your cart'))
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.artwork} to your cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.artwork} '
                              f'quantity to {cart[item_id]}'))
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.artwork} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f"Updated {product.artwork} (size {size.upper()}) quantity to {cart[item_id]['items_by_size'][size]}")

        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f"{product.artwork} (size {size.upper()}) removed from your art cart")

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f"{product.artwork} quantity updated to {cart[item_id]}")
        else:
            cart.pop(item_id)
            messages.success(request, f"{product.artwork} removed from your art cart")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[product_id]['items_by_size'][size]
            if not cart[product_id]['items_by_size']:
                cart.pop(product_id)
            messages.success(request, f"{product.artwork} (size {size.upper()}) removed from your art cart")

        else:
            cart.pop(product_id)
            messages.success(request, f"{product.artwork} removed from your art cart")

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
