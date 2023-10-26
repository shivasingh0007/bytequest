from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from proapp.models import Category,Products
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password','is_staff')
        # extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')

        # Create a new User instance with the remaining data
        user = User(**validated_data)

        # Set the password for the user
        user.set_password(password)

        # Save the user to the database
        user.save()

        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['product_name','product_image','product_qty','product_price','category']