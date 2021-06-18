# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse

import requests
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from orders.models import Order


@csrf_exempt
def payment_done(request, id):
    order = get_object_or_404(Order, id=id)
    order.paid = True
    order.save()
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return render(request, 'payment/canceled.html')


def vndToUsd(amount):
    r = requests.get('http://data.fixer.io/api/latest?access_key=a765f24ed8b5fba63fd7b27f08641149')
    y = r.json()
    a = y["rates"]["USD"]
    b = y["rates"]["VND"]
    return amount*a/b;


def payment_process(request, id):
    order = get_object_or_404(Order, id=id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': vndToUsd(float(order.get_total_cost())),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done', args=[id])),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled', args=[id])),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'form': form})
