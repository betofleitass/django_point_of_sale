from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category


@login_required(login_url="/accounts/login/")
def CategoriesListView(request):
    context = {
        "active_icon": "products_categories"
    }
    return render(request, "products/categories.html", context=context)


@login_required(login_url="/accounts/login/")
def CategoriesAddView(request):
    context = {
        "active_icon": "products_categories",
        "category_status": Category.status.field.choices
    }

    if request.method == 'POST':
        # Save the POST arguements
        data = request.POST

        name = data['name']
        status = data['state']
        description = data['description']

        # Create the category
        new_category = Category.objects.create(
            name=name,
            status=status,
            description=description
        )

        new_category.save()

        messages.success(request, 'Category: ' +
                         name + ' created succesfully!', extra_tags="success")
        return redirect('products:categories_list')

    return render(request, "products/categories_add.html", context=context)
