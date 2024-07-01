from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_products, name='products'),
    path('<int:product_id>/', views.artwork_details, name='artwork_details'),
    path('create/', views.create_product, name='create_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
]