import os
from djongo import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Products(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=255)
     image = models.ImageField(upload_to="uploads", height_field=None, width_field=None, max_length=None)
     category = models.CharField(max_length=100)
     selling_price = models.CharField(max_length=100)
     mrp = models.CharField(max_length=100)

def __str__(self):
        return self.name

def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(Products, self).delete(*args, **kwargs)