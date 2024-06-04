from django.db import models
from django.contrib.auth.models import User

from shop.models import Shop


class Favorites(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Shop, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'products')

    def __str__(self):
        return f"{self.user.first_name} - {self.products.title}"

