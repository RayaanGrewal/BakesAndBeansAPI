from .models import Item
from rest_framework import serializers

class ItemCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['itemName' , 'ingredients', 'price' , "veg" ,"nonVeg" , "pk"]
