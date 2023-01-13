from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product, Category


@login_required(login_url="/accounts/login/")
def index(request):
    context = {
        "active_icon": "dashboard",
        "products": Product.objects.all().count(),
        "categories": Category.objects.all().count()
    }
    return render(request, "pos/index.html", context)
