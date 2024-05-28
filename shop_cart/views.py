from django.shortcuts import render, redirect


def view_cart(request):
    # A view to render the shopping cart
    return render(request, 'cart/cart.html')


def add_to_cart(request, artwork_id):
    # Add a product to the view_cart

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if artwork_id in list(cart.keys()):
        cart[artwork_id] += quantity
    else:
        cart[artwork_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)