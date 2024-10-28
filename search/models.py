# search/models.py
from django.db import models

class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, unique=True)
    subcategory = models.ForeignKey(SubCategory, related_name='prosubcat', on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=None, blank=True, null=True)  # Discount can be optional
    title = models.CharField(max_length=225)
    description = models.TextField()
    overview = models.TextField(null=True, blank=True)
    featured = models.BooleanField(null=True)
    image = models.ImageField(blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title