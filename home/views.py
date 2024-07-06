from django.shortcuts import render


def home_view(request):
    # A view to return the home page
    return render(request, 'home/index.html')
