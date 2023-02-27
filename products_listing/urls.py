from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('products', views.getProducts, name='products'),
    path('add_product', views.add_product, name='add_product'),
]