from rest_framework import serializers
from .models import Order, Item, Product
from member.models import Member

class CreateItem(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    count = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Item
        fields = ['product', 'count', 'price']

    def validate(self, attrs):
        product = attrs.get('product')
        count = attrs.get('count')
        attrs['price'] = product.price * count
        return attrs
    
    def to_internal_value(self, data):
        product_data = data.get('product')
        product_instance = Product.objects.get(name=product_data['name'])
        # 將 product 字典替換為其主鍵
        data['product'] = product_instance.pk  
        return super().to_internal_value(data)

class CreateOrder(serializers.ModelSerializer):
    items = CreateItem(many=True)
    member = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'addressee', 'address', 'tel', 'total_amount', 'member', 'items']
        read_only_fields = ['id']
    
    def to_internal_value(self, data):
        # 解析 member
        member_data = data.get('member')
        member = Member.objects.get(name=member_data['name'])
        # 將 member 字典替换為主键
        data['member'] = member.pk  
        # 更新會員的地址和電話
        member.address = data.get('address')
        member.tel = data.get('tel')
        member.save()
        return super().to_internal_value(data)

    def create(self, validated_data):
        # 先從 validated_data 中提取 items 資料
        items_data = validated_data.pop('items')

        # 創建訂單
        order = Order.objects.create(**validated_data)

        # 為訂單創建相關的 items
        for item_data in items_data:
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
        fields= ['id', 'status', 'created_at', 'total_amount', 'addressee', 'address', 'tel', 'items', 'member']