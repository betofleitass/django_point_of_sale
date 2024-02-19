from django.urls import path

from . import views

app_name = "customers"
urlpatterns = [
    # List customers
    path('', views.customers_list_view, name='customers_list'),
    # Add customer
    path('add', views.customers_add_view, name='customers_add'),
    # Update customer
    path('update/<str:customer_id>',
         views.customers_update_view, name='customers_update'),
    # Delete customer
    path('delete/<str:customer_id>',
         views.customers_delete_view, name='customers_delete'),
]
