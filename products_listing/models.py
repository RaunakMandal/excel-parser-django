from django.db import models
import uuid

class Product(models.Model):
    uid = models.UUIDField(primary_key=True, max_length=24, default=uuid.uuid4, unique=True, editable=False)
    name = models.TextField()
    lowest_price = models.TextField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

class ProductVariation(models.Model):
    uid = models.UUIDField(primary_key=True, max_length=24, default=uuid.uuid4, unique=True, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_text = models.TextField()
    stock = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)