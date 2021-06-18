# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from shop.models import Product
from accounts.models import User
from decimal import Decimal


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    PAYMENT_CHOICES = (('0', 'Thanh toán khi nhận hàng'), ('1', 'Thanh toán bằng paypal'))
    payment_type = models.CharField(max_length=1, choices=PAYMENT_CHOICES, blank=True, default='0')
    paid = models.BooleanField(default=False)
    STATE_CHOICES = (('0', 'Chờ xác nhận'), ('1', 'Đã xác nhận'), 
        ('2', 'Đang giao hàng'), ('3', 'Giao hàng thành công'), ('4', 'Huỷ'), ('5', 'Giao hàng thất bại'))
    state = models.CharField(max_length=1, choices=STATE_CHOICES, blank=True, default='0')
    shipment_name = models.CharField(max_length=50, null=True, blank=True, default='Giao hàng tiết kiệm')
    shipment_price = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True, default=Decimal('10000'))

    class Meta: 
        ordering = ('-created',)

    def __str__(self):
        return 'Order {} {}'.format(self.user, self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all()) + self.shipment_price;


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)
    isComment = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.price * self.quantity