from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.TextField()
    friendly_name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    art_category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_num = models.CharField(max_length=80, null=True, blank=True)
    artwork = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    art_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.artwork
