from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    # List categories
    path('categories', views.CategoriesListView, name='categories_list'),
    # Add category
    path('categories/add', views.CategoriesAddView, name='categories_add'),
    # Update category
    path('categories/update/<str:category_id>',
         views.CategoriesUpdateView, name='categories_update'),
    # Delete category
    path('categories/delete/<str:category_id>',
         views.CategoriesDeleteView, name='categories_delete'),

    # List products
    path('', views.ProductsListView, name='products_list'),
    # Add product
    path('add', views.ProductsAddView, name='products_add'),
    # Update product
    path('update/<str:product_id>',
         views.ProductsUpdateView, name='products_update'),
    # Delete product
    path('delete/<str:product_id>',
         views.ProductsDeleteView, name='products_delete'),
    # Get products AJAX
    path("get", views.GetProductsAJAXView, name="get_products"),
]
