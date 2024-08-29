from rest_framework import serializers
from shop.models import Product, ProductPhoto

class CreatePhoto(serializers.ModelSerializer):
    class Meta:
        model= ProductPhoto
        fields= ['photo', 'description']

class CreateProduct(serializers.ModelSerializer):
    
    class Meta:
        model= Product
        fields= ['name', 'icon', 'introduction', 'description', 'price']

class GetPhoto(serializers.ModelSerializer):
    class Meta:
        model= ProductPhoto
        fields= ['photo', 'description']

class GetProduct(serializers.ModelSerializer):
    photos = GetPhoto(many=True)
    
    class Meta:
        model= Product
        fields= ['name', 'date', 'icon', 'introduction', 'description', 'price', 'count', 'photos']
        
