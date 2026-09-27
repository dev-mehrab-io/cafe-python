from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    ingredients = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(null=True, upload_to='menu_photos')

    def __str__(self):
        return self.name