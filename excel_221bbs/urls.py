from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('products_listing.urls')),
    # path('admin/', admin.site.urls),
]