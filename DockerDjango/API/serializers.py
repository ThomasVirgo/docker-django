from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')
        write_only_fields = ('password', 'password_confirmation')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        password=validated_data['password']
        password_confirmation=validated_data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError({'password': 'Passwords must match.'}) 
        user.set_password(password)
        user.save()

        return user   

class RestaurantSerializer(serializers.ModelSerializer):
     class Meta:
         model = Restaurant
         fields = '__all__'