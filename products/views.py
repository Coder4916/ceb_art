from django.shortcuts import render, get_object_or_404
from .models import Product


#A view to render the art_products
def art_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/art_products.html', context)


#A view to render the artwork details
def artwork_details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/artwork_details.html', context)
