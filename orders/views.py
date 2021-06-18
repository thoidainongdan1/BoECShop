# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from cart.models import Cart
from comment.models import Comment
from payment.models import Shipment
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


@login_required
def order_save(request):
    order = Order.objects.create(user=request.user)
    cart = Cart.objects.get(user=request.user)

    for item in cart.items.all(): 
        orderItem, created = OrderItem.objects.update_or_create(
            order=order, product=item.product, price=item.product.price, quantity=item.quantity)

        order.items.add(orderItem)

    profile = Profile.objects.get(user=request.user)
    profile.full_name = request.POST['full_name']
    phone_number = request.POST['phone_number']
    if profile.phone_number == '':
        profile.phone_number = phone_number
    profile.address = request.POST['address']
    order.phone_number = phone_number
    order.address_second = request.POST['address_second']
    order.payment_type = request.POST['payment_type']
    shipment = Shipment.objects.get(id=request.POST['shipment_type'])
    order.shipment_name = shipment.name
    order.shipment_price = shipment.price
    profile.save()
    order.save()
    cart.delete() 

    if order.payment_type == "1":
        return redirect('../../payment/' + str(order.id) + '/process')
    else:
        return render(request, 'orders/order_success.html')


@login_required
def order_create(request):
    profile = get_object_or_404(Profile, user=request.user)
    cart = Cart.objects.get(user=request.user)
    shipment = Shipment.objects.all()

    return render(request, 'orders/order_form.html', {'cart': cart, 'profile': profile, 'shipment': shipment})


@login_required
def order_list(request):
    if not Order.objects.filter(user=request.user).exists():
        return render(request, 'orders/order_list.html', {'empty': "yes"})
    else:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_remove(request, order_id):
    order, created = Order.objects.update_or_create(id=order_id)
    order.state = '4'
    order.save()

    return redirect('orders:order_list')


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_comment(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_comment.html', {'order': order})


@user_passes_test(lambda u: u.is_superuser)
def check_order(request):
    orders = Order.objects.all()
    if not orders:
        return render(request, 'orders/order_list_admin.html', {'empty': "yes"})
    else:
        return render(request, 'orders/order_list_admin.html', {'orders': orders})


@login_required
def order_change_state(request, order_id):
    order = Order.objects.get(id=order_id)
    order.state = request.GET['order_state']
    if order.state == '3':
        order.paid = True
    order.save()
    return redirect('orders:check_order')