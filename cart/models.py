
from django.db import models

from product.models import Product

from home.models import Account


class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    is_in_order = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return 'cart {}'.format(self.user.email if self.user else 'Anonymous')

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.cart_items.all()) if self.cart_items.exists() else 0

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products_in_cart', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.product.name)

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        super().save(*args, **kwargs)
