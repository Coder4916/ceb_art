from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_products, name='products'),
    path('<product_id>', views.artwork_details, name='artwork_details'),
]