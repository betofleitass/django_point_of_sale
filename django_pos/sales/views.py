from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from customers.models import Customer
from .models import Sale, SaleDetail
from products.models import Product
import json


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required(login_url="/accounts/login/")
def SalesListView(request):
    context = {
        "active_icon": "sales",
        "sales": Sale.objects.all()
    }
    return render(request, "sales/sales.html", context=context)


@login_required(login_url="/accounts/login/")
def SalesAddView(request):
    context = {
        "active_icon": "sales",
        "customers": [c.to_select2() for c in Customer.objects.all()]
    }

    if request.method == 'POST':
        if is_ajax(request=request):
            # Save the POST arguements
            data = json.load(request)

            sale_attributes = {
                "customer": Customer.objects.get(id=int(data['customer'])),
                "sub_total": float(data["sub_total"]),
                "grand_total": float(data["grand_total"]),
                "tax_amount": float(data["tax_amount"]),
                "tax_percentage": float(data["tax_percentage"]),
                "amount_payed": float(data["amount_payed"]),
                "amount_change": float(data["amount_change"]),
            }
            try:
                # Create the sale
                new_sale = Sale.objects.create(**sale_attributes)
                new_sale.save()
                # Create the sale details
                products = data["products"]

                for product in products:
                    detail_attributes = {
                        "sale": Sale.objects.get(id=new_sale.id),
                        "product": Product.objects.get(id=int(product["id"])),
                        "price": product["price"],
                        "quantity": product["quantity"],
                        "total_detail": product["total_product"]
                    }
                    sale_detail_new = SaleDetail.objects.create(
                        **detail_attributes)
                    sale_detail_new.save()

                messages.success(
                    request, 'Sale created succesfully!', extra_tags="success")
                return redirect('sales:sales_list')
            except Exception as e:
                messages.success(
                    request, 'There was an error during the creation!', extra_tags="danger")
                print(e)
                return redirect('sales:sales_list')

    return render(request, "sales/sales_add.html", context=context)


@login_required(login_url="/accounts/login/")
def SalesDetailsView(request, sale_id):
    """
    Args:
        sale_id: ID of the sale to view
    """
    try:
        # Get tthe sale
        sale = Sale.objects.get(id=sale_id)

        # Get the sale details
        details = SaleDetail.objects.filter(sale=sale)

        context = {
            "active_icon": "sales",
            "sale": sale,
            "details": details,
        }
        return render(request, "sales/sales_details.html", context=context)
    except Exception as e:
        messages.success(
            request, 'There was an error getting the sale!', extra_tags="danger")
        print(e)
        return redirect('sales:sales_list')
