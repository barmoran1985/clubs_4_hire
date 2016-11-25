from django.shortcuts import render, get_object_or_404, redirect, reverse
from models import CartItem
from django.contrib.auth.decorators import login_required
from products.models import Product


@login_required(login_url="/login?next=cart")
def user_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.product.price

    return render(request, "cart.html", {"items": cart_items, 'total': total})


@login_required(login_url="/login?next=cart/add")
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    cart_item = CartItem(
        user=request.user,
        product=product,
        quantity=1
    )
    cart_item.save()
    return redirect(reverse('cart'))


def remove_from_cart(request, id):
    CartItem.objects.get(id=id).delete()
    return redirect(reverse('cart'))
