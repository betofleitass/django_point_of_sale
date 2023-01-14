from datetime import date
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField, F
from django.db.models.functions import Coalesce
from django.shortcuts import render
from products.models import Product, Category
from sales.models import Sale, SaleDetail


@login_required(login_url="/accounts/login/")
def index(request):
    today = date.today()

    year = today.year

    context = {
        "active_icon": "dashboard",
        "products": Product.objects.all().count(),
        "categories": Category.objects.all().count(),
        "annual_earnings": Sale.objects.filter(date_added__year=year).aggregate(total_variable=Coalesce(Sum(F('grand_total')), 0.0, output_field=FloatField())).get('total_variable')
    }
    return render(request, "pos/index.html", context)
