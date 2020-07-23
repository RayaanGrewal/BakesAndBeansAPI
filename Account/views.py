from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions , authentication
from rest_framework.authtoken.models import Token

from .serializer import UserRegisterSerializer
from .models import User


class UserRegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self , request):
        if request.method == "POST":
            data = {}
            serializer = UserRegisterSerializer(data = request.data)

            if serializer.is_valid():
                user = serializer.save()
                data['response'] = "Succesful user registeration."
                data['email'] = user.email
                data['password'] = user.password
                token = Token.objects.get(user=user).key
                data['token'] = token

            else:
                data = serializer.errors

        return Response(data)
