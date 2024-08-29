from rest_framework import serializers
from .models import Order, Item, Product
from member.models import Member


class CreateItem(serializers.ModelSerializer):
    product= serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model= Item
        fields= ['product', 'count', 'price']

class CreateOrder(serializers.ModelSerializer):
    items= CreateItem(many= True)  # 嵌套的訂單商品序列化器
    member= serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())

    class Meta:
        model= Order
        fields= ['id', 'addressee', 'address', 'tel', 'total_amount', 'member', 'items']

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        
        # 將 address 和 tel 從 validated_data 中提取出來
        # 更新會員的 address 和 tel 資料
        member = order.member
        member.address = validated_data.pop('address')
        member.tel = validated_data.pop('tel')
        member.save()
        
        for item_data in validated_data.pop('items'):
            Item.objects.create(order=order, **item_data)
        
        return order

class GetMember(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['name', 'display_name', 'email', 'role', 'created_at']
        
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
    items= GetItem(many=True, read_only=True)
    member= GetMember(read_only=True)
    
    class Meta:
        model= Order
        fields= ['id', 'status', 'created_at', 'total_amount', 'address', 'tel', 'items', 'member']