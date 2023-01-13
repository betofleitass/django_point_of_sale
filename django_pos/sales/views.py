from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sales.models import Customer


@login_required(login_url="/accounts/login/")
def SalesListView(request):
    context = {
        "active_icon": "sales",
        "sales": Customer.objects.all()
    }
    return render(request, "sales/sales.html", context=context)


@login_required(login_url="/accounts/login/")
def SalesAddView(request):
    context = {
        "active_icon": "sales",
        "customers": [c.to_select2() for c in Customer.objects.all()]
    }

    print(context["customers"])

    if request.method == 'POST':
        # Save the POST arguements
        data = request.POST

        attributes = {
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "address": data['address'],
            "email": data['email'],
            "phone": data['phone'],
        }

        # Check if a sale with the same attributes exists
        if Customer.objects.filter(**attributes).exists():
            messages.error(request, 'Customer already exists!',
                           extra_tags="warning")
            return redirect('sales:sales_add')

        try:
            # Create the sale
            new_customer = Customer.objects.create(**attributes)

            # If it doesn't exists save it
            new_customer.save()

            messages.success(request, 'Customer: ' + attributes["first_name"] + " " +
                             attributes["last_name"] + ' created succesfully!', extra_tags="success")
            return redirect('sales:sales_list')
        except Exception as e:
            messages.success(
                request, 'There was an error during the creation!', extra_tags="danger")
            print(e)
            return redirect('sales:sales_add')

    return render(request, "sales/sales_add.html", context=context)
