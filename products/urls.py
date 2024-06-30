from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_products, name='products'),
    path('<int:product_id>/', views.artwork_details, name='artwork_details'),
    path('add/', views.add_product, name='add_product'),
]