from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def CategoriesListView(request):
    context = {
        "active_icon": "products_categories"
    }
    return render(request, "products/categories.html", context=context)


@login_required(login_url="/accounts/login/")
def CategoriesAddView(request):
    context = {
        "active_icon": "products_categories"
    }
    return render(request, "products/categories_add.html", context=context)
