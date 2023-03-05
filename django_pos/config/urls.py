
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication: Login and Logout
    path('', include('django_pos.authentication.urls')),
    # Index
    path('', include('django_pos.pos.urls')),
    # Products
    path('products/', include('django_pos.products.urls')),
    # Customers
    path('customers/', include('django_pos.customers.urls')),
    # Sales
    path('sales/', include('django_pos.sales.urls')),
]
