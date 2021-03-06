from django.db import models


class Item(models.Model):
    itemName = models.CharField(max_length = 30)
    ingredients = models.CharField(max_length= 80)
    price = models.IntegerField()
    veg = models.BooleanField()
    nonVeg = models.BooleanField()

    def __str__(self):
        return self.itemName
