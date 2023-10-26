from django.shortcuts import render
from .models import Category,Products
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,permissions
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# from proapp.permission import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, CategorySerializer,ProductsSerializer
from rest_framework.permissions import AllowAny

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def get_data():
    data = cache.get('my_key')
    if data is None:
        data = Products.objects.filter(...)  # Query the database
        cache.set('my_key', data, timeout=3600)  # Cache the result for 1 hour
    return data


class CategoryCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

class CategoryUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductsCreate(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ProductsUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]