from rest_framework import serializers
from .models import Member
from shop.models import Order, OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ['name', 'price']

class ItemSerializer(serializers.ModelSerializer):
    product= ProductSerializer(many= True)  # 嵌套的商品序列化器

    class Meta:
        model= OrderItem
        fields= ['product', 'count']

class OrderSerializer(serializers.ModelSerializer):
    items= ItemSerializer(many= True)  # 嵌套的訂單商品序列化器

    class Meta:
        model= Order
        fields= ['id', 'status', 'created_at', 'total_amount', 'address', 'tel', 'items']

class MemberSerializer(serializers.ModelSerializer):
    order= OrderSerializer(many= True)  # 嵌套的訂單序列化器

    class Meta:
        model= Member
        fields= ['name', 'display_name', 'icon', 'email', 'verification', 'address', 'tel', 'created_at', 'role', 'order']

class CreateMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model= Member
        fields= ['name', 'password', 'display_name', 'email', 'created_at', 'role']
    
    
