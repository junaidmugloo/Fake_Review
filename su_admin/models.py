from djongo import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Products(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=255)
     image = models.CharField(max_length=255)
     category = models.CharField(max_length=100)
     selling_price = models.CharField(max_length=100)
     mrp = models.CharField(max_length=100)