

from django.shortcuts import render, redirect, get_object_or_404

from product.models import Product
from .models import Cart, CartItem

from django.contrib.auth.decorators import login_required



@login_required
def cart_add(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(cart=obj, product=product)
    
    item.price = product.price
    if not itemCreated:
        item.quantity += 1

    item.save()  # This saves the updated quantity and price
    
    return redirect('cart:cart_detail')


@login_required
def cart_add_q(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(cart=obj, product=product)
    
    item.price = product.price
    q = request.GET.get('q', 1)  # Default to 1 if 'q' is not provided
    try:
        item.quantity = int(q)  # Cast to integer
        if item.quantity <= 0:  # Prevent invalid quantity like zero or negative
            item.delete()
        else:
            item.save()
    except ValueError:
        # Handle if 'q' is not a valid integer
        item.quantity = 1
        item.save()
    
    return redirect('cart:cart_detail')

@login_required
def cart_remove(request, product_id):
    try:
        obj = Cart.objects.get(user=request.user)
        product = get_object_or_404(Product, id=product_id)
        CartItem.objects.filter(cart=obj, product=product).delete()
    except Cart.DoesNotExist:
        pass  # Handle if no cart exists (optional)
    
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None  # Or redirect to a different page if needed
    
    return render(request, 'cart/cart_detail.html', {'cart': cart})
