from rest_framework import serializers
from .models import Member
from order.models import Order, Item, Product

class GetProduct(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= ['name', 'price']
        
class GetItem(serializers.ModelSerializer):
    product= GetProduct(read_only=True)

    class Meta:
        model= Item
        fields= ['product', 'count', 'price']

class GetOrder(serializers.ModelSerializer):
    items= GetItem(read_only=True, many=True)

    class Meta:
        model= Order
        fields= ['id', 'status', 'created_at', 'total_amount', 'address', 'tel', 'items']

class GetMember(serializers.ModelSerializer):
    order= GetOrder(many= True)  # 嵌套的訂單序列化器

    class Meta:
        model= Member
        fields= ['name', 'display_name', 'icon', 'email', 'verification', 'address', 'tel', 'created_at', 'role', 'order']

class CreateMember(serializers.ModelSerializer):

    class Meta:
        model= Member
        fields= ['name', 'password', 'email']
    
    
