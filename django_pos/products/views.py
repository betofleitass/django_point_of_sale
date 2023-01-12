from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category


@login_required(login_url="/accounts/login/")
def CategoriesListView(request):
    context = {
        "active_icon": "products_categories",
        "categories": Category.objects.all()
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

        attributes = {
            "name": data['name'],
            "status": data['state'],
            "description": data['description']
        }

        # Check if a category with the same attributes exists
        if Category.objects.filter(**attributes).exists():
            messages.error(request, 'Category already exists!',
                           extra_tags="warning")
            return redirect('products:categories_add')

        try:
            # Create the category
            new_category = Category.objects.create(**attributes)

            # If it doesn't exists save it
            new_category.save()

            messages.success(request, 'Category: ' +
                             attributes["name"] + ' created succesfully!', extra_tags="success")
            return redirect('products:categories_list')
        except Exception as e:
            messages.success(
                request, 'There was an error during the creation!', extra_tags="danger")
            print(e)
            return redirect('products:categories_add')

    return render(request, "products/categories_add.html", context=context)


@login_required(login_url="/accounts/login/")
def CategoriesDeleteView(request, category_id):
    """
    Args:
        category_id : The category's ID that will be deleted
    """
    try:
        # Get the category to delete
        category = Category.objects.get(id=category_id)
        category.delete()
        messages.success(request, '¡Category: ' + category.name +
                         ' deleted!', extra_tags="success")
        return redirect('products:categories_list')
    except Exception as e:
        messages.success(
            request, 'There was an error during the elimination!', extra_tags="danger")
        print(e)
        return redirect('products:categories_list')


@login_required(login_url="/accounts/login/")
def CategoriesUpdateView(request, category_id):
    """
    Args:
        category_id : The category's ID that will be updated
    """

    # Get the category
    try:
        # Get the category to delete
        category = Category.objects.get(id=category_id)
    except Exception as e:
        messages.success(
            request, 'There was an error trying to get the category!', extra_tags="danger")
        print(e)
        return redirect('products:categories_list')

    context = {
        "active_icon": "products_categories",
        "category_status": Category.status.field.choices,
        "category": category
    }

    if request.method == 'POST':
        try:
            # Save the POST arguements
            data = request.POST

            attributes = {
                "name": data['name'],
                "status": data['state'],
                "description": data['description']
            }

            # Get the category to update
            category = Category.objects.filter(
                id=category_id).update(**attributes)

            category = Category.objects.get(id=category_id)

            messages.success(request, '¡Category: ' + category.name +
                             ' updated successfully!', extra_tags="success")
            return redirect('products:categories_list')
        except Exception as e:
            messages.success(
                request, 'There was an error during the elimination!', extra_tags="danger")
            print(e)
            return redirect('products:categories_list')

    return render(request, "products/categories_update.html", context=context)