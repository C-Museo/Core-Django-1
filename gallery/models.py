from django.db import models

# Create your models here.
#Image
#Image Name.
#Image Description.
#Image Location Foreign Key.
#Image category Foreign Key.

class Image(models.Model):
    image_name=models.CharField(max_length =30)
    image_decsription=models.CharField(max_length =30)
    image_location=models.CharField(max_length =30)
    image_category=models.CharField(max_length =30)

class Location(models.Model):
    location_description=models.CharField(max_length=30)

class Category (models.Model):
    category_description=models.CharField(max_length=30)