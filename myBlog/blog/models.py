# myapp/models.py
from django.db import models

class Category(models.TextChoices):
    WOOD = 'wood', 'Wood Related'
    PRINTING = 'printing', '3D Printing'
    ELECTRONICS = 'electronics', 'Electronics'
    OTHERS = 'others', 'Others'

class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=Category.choices)

    def __str__(self):
        return self.title
