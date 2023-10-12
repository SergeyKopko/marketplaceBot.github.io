from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
# Create your models here.
