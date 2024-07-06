from django.shortcuts import render
from .models import Username, Review


# A view to render the about_us page
def about_us(request):

    reviews = Review.objects.all()
    usernames = Username.objects.all()

    context = {
        'reviews': reviews,
        'usernames': usernames,
    }

    return render(request, 'about_us/about_us.html', context)
