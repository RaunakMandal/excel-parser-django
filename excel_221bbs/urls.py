from django.urls import include, path

urlpatterns = [
    path('', include('products_listing.urls')),
]