from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserImageModel(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    
    def __str__(self):
        return str(self.image)
