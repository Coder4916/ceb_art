from django.shortcuts import render, redirect


def view_cart(request):
    # A view to render the shopping cart
    return render(request, 'cart/cart.html')


def add_to_cart(request, artwork_id):
    # Add a product to the view_cart

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