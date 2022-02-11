from distutils.command.upload import upload
from enum import unique
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("category_list", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default="")
    p_name = models.CharField(max_length=200, null=False)
    p_price = models.FloatField()
    p_desc = models.TextField(max_length=500)
    p_image = models.ImageField(
        upload_to="products/", default="products/m2.png")
    slug = models.SlugField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.p_name

    def get_absolute_url(self):
        return reverse("product_details", args=[self.slug])
