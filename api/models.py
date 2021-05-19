from django.db import models

# Create your models here.

class image(models.Model):
   img = models.ImageField(upload_to="images_api", default="") 

   def __str__(self):
        return self.product_name