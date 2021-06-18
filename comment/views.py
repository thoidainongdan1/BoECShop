from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from shop.models import Product
from orders.models import *
from .models import *

# Create your views here.

@login_required
def comment_save(request, product_id, order_id):
    comment = Comment.objects.create(user=request.user)
    comment.product = Product.objects.get(id=product_id)
    comment.star = request.POST['rate']
    comment.content = request.POST['comment_content']
    comment.save()

    order = Order.objects.get(id=order_id)
    product = Product.objects.get(id=product_id)
    order_item = order.items.get(product=product)
    order_item.isComment = True
    order_item.save()

    return redirect('orders:order_comment', order_id=order_id)