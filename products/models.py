from django.db import models
from sellers.models import SellerProfile


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=55.55)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title