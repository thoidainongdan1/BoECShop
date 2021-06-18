# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Shipment(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return '{} ({}đ)'.format(self.name, self.price)