from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    lowest_price = models.TextField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

class ProductVariation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_text = models.TextField()
    stock = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)