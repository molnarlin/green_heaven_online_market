from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CareInfo(models.Model):
    light = models.CharField(max_length=100)
    water = models.CharField(max_length=300)
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    care_info = models.JSONField(null=True, blank=True)
    fertilizer = models.CharField(max_length=300, null=True, blank=True)
    pests = models.CharField(max_length=300, null=True, blank=True)
    pruning = models.CharField(max_length=300, null=True, blank=True)
    repotting = models.CharField(max_length=300, null=True, blank=True)
    delivery = models.CharField(max_length=300, null=True, blank=True)
    planting = models.CharField(max_length=300, null=True, blank=True)
    harvesting = models.CharField(max_length=300, null=True, blank=True)
    size = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
