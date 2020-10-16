from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
#Image
#Image Name.
#Image Description.
#Image Location Foreign Key.
#Image category Foreign Key.

class Image(models.Model):
    image=CloudinaryField('image')
    image_description=models.CharField(max_length =30)
    #image_location=models.CharField(max_length =30)
    #image_category=models.CharField(max_length =30)

    def _str_self(self):
        return self.image_description
    objects = models.Manager()
    
    class Meta:
        verbose_name_plural=('Images')

class Location(models.Model):
    location_description=models.CharField(max_length=30)

class Category (models.Model):
    category_description=models.CharField(max_length=30)