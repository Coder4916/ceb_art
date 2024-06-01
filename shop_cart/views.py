from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from products.models import Product


def view_cart(request):
    # A view to render the shopping cart page
    return render(request, 'cart/cart.html')


def add_to_cart(request, artwork_id):
    # Add an art product to the cart

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'artwork_size' in request.POST:
        size = request.POST['artwork_size']
        cart = request.session.get('cart', {})

    if size:
        if artwork_id in list(cart.keys()):
            if size in cart[artwork_id]['items_by_size'].keys():
                cart[artwork_id]['items_by_size'][size] += quantity
            else:
                cart[artwork_id]['items_by_size'][size] = quantity
        else:
            cart[artwork_id] = {'items_by_size': {size: quantity}}
    else:
        if artwork_id in list(cart.keys()):
            cart[artwork_id] += quantity
        else:
            cart[artwork_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, artwork_id):
# Adjust the art products in the cart

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    cart = request.session.get('cart', {})
    
    if size:
        if quantity > 0:
            cart[artwork_id]['items_by_size'][size] = quantity
        else:
            del cart[artwork_id]['items_by_size'][size]
    else:
        if quantity > 0:
            cart[artwork_id] = quantity
        else:
            cart.pop[artwork_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))