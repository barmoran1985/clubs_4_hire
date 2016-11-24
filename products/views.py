from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "productdetail.html", {'product': product})
