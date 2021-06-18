# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required


@login_required
def cart_add(request, product_id):
    cart, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(
        cart=cart, product=product)

    if(itemCreated == False):
        item.quantity = item.quantity+1

    cart.items.add(item)
    item.save()
    cart.save()
    return redirect('cart:cart_detail')


@login_required
def cart_add_quantity(request, product_id, product_qty=None):
    cart, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(
        cart=cart, product=product)

    item.quantity = request.GET['quantity']
    if request.GET['quantity'] == "0":
        item.delete()
    else:
        cart.items.add(item)
        item.save()
        cart.save()
    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, product_id):
    cart, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cartItems = CartItem.objects.filter(cart=cart, product=product)
    cartItems.delete()
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart, created = Cart.objects.update_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
