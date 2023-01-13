from django.urls import path

from . import views

app_name = "customers"
urlpatterns = [
    # List customers
    path('', views.CustomersListView, name='customers_list'),
    # Add customer
    path('add', views.CustomersAddView, name='customers_add'),
    # Update customer
    path('update/<str:customer_id>',
         views.CustomersUpdateView, name='customers_update'),
    # Delete customer
    path('delete/<str:customer_id>',
         views.CustomersDeleteView, name='customers_delete'),
]
