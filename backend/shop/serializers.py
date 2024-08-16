from rest_framework import serializers
from shop.models import Order, OrderItem, Product, ProductPhoto

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductPhoto
        fields= ['photo', 'description']

class ProductSerializer(serializers.ModelSerializer):
    photo= PhotoSerializer(many= True)
    
    class Meta:
        model= Product
        fields= ['name', 'Introduction', 'description', 'price', 'photo']

class ItemSerializer(serializers.ModelSerializer):
    product= ProductSerializer(many= True)  # 嵌套的商品序列化器

    class Meta:
        model= OrderItem
        fields= ['product', 'count', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items= ItemSerializer(many= True)  # 嵌套的訂單商品序列化器

    class Meta:
        model= Order
        fields= ['id', 'status', 'member', 'address', 'tel', 'created_at', 'total_amount', 'items']

