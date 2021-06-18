from django.db import models
from shop.models import Product
from accounts.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_comments" , on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    star = models.PositiveIntegerField(null=True)
    content = models.CharField(max_length=200)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment {} {} {}'.format(self.user, self.product, self.id)