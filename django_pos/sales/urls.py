from django.urls import path

from . import views

app_name = "sales"
urlpatterns = [
    # List sales
    path('', views.SalesListView, name='sales_list'),
    # Add sale
    path('add', views.SalesAddView, name='sales_add'),
    # Details sale
    path('details/<str:sale_id>',
         views.SalesDetailsView, name='sales_details'),
]
