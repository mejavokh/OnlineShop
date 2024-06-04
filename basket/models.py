from django.db import models
from shop.models import Shop
from django.contrib.auth.models import User


class Basket(models.Model):
    product = models.ForeignKey(to=Shop,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Корзина для: {self.user.username} | Продукт: {self.product.title}'

    def sum(self):
        return self.product.price * self.quantity


