from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


#A view to render the art_products
def art_products(request):

    products = Product.objects.all()
    search = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(art_category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(request, "No search request!")
                return redirect(reverse ('products'))

            searches = Q(artwork__icontains=search) | Q(description__icontains=search)
            products = products.filter(searches)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'current_categories': categories,
        'sorting': sorting,
    }
    return render(request, 'products/art_products.html', context)


#A view to render the artwork details
def artwork_details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/artwork_details.html', context)
