from .models import User
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'} ,  write_only=True)

    class Meta:
        model = User
        fields = ['email' , 'password' ,'password2']
        extra_kwargs = {'password' : {'write_only':True}}

    def save(self):
        user = User(email = self.validated_data['email'])

        p1 = self.validated_data['password']
        p2 = self.validated_data['password2']

        if p1 != p2 :
            raise serializers.ValidationError({'password': 'Password\'s do not match'})

        user.set_password(p1)

        user.save()

        return user
