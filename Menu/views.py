from django.shortcuts import render

from django.shortcuts import render
from .models import Item
from .serializer import ItemCRUDSerializer

from rest_framework.views import APIView
from rest_framework import permissions , authentication
from rest_framework.response import Response

from rest_framework.authtoken.models import Token


class ItemCRUDView(APIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self , request):
        if request.method == "POST":
            data = {}
            serializer = ItemCRUDSerializer(data=request.data)

            if serializer.is_valid():
                item = serializer.save()
                data['response'] = "Successful creation of Item"
                data['itemName'] = item.itemName
                data['ingredients'] = item.ingredients
                data['price'] = item.price
            else :
                data = serializer.errors

            return Response(data=data)
