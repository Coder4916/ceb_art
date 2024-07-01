from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


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
            if sortkey == 'category':
                sortkey = 'category__name'
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
                messages.error(request, "No search request entered!")
                return redirect(reverse ('products'))

            searches = Q(artwork__icontains=search) | Q(description__icontains=search) | Q(art_image__icontains=search)
            products = products.filter(searches)

    sorting = f'{sort}_{direction}'
    categories = Category.objects.all()
    context = {
        'products': products,
        'search_term': search,
        'current_categories': categories,
        'current_sorting': sorting,
    }
    return render(request, 'products/art_products.html', context)


#A view to render the artwork details
def artwork_details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/artwork_details.html', context)


def add_product(request):
    # Add an art product to the store
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)