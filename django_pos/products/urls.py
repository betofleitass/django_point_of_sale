from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    # List categories
    path('categories', views.CategoriesListView, name='categories_list'),
    # Add category
    path('categories/add', views.CategoriesAddView, name='categories_add'),
    # Delete category
    path('categories/delete/<str:category_id>',
         views.CategoriesDeleteView, name='categories_delete'),
    # Update category
    path('categories/update/<str:category_id>',
         views.CategoriesUpdateView, name='categories_update'),

    # List products
    path('', views.ProductsListView, name='products_list'),
    # Add category
    path('add', views.ProductsAddView, name='products_add'),
]
