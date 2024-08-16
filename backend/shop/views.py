from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import OrderSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from decorators import try_except
from .models import Order, Product

# 建立訂單
@api_view(['POST'])
@try_except
def create_order(request):
    
    serializer= OrderSerializer(data= request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f"save order {serializer.data}", 'data': serializer.data}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 取得一筆訂單
@api_view(['GET'])
@try_except
def get_order(request):
    
    order= Order.objects.get(id= request.GET.get('id'))
    
    serializer= OrderSerializer(order)
    
    return Response(serializer.data)
    
# 更新訂單
@api_view(['PUT'])
@try_except
def update_order(request):
    
    order= Order.objects.get(id= request.POST.get('id'))
    
    serializer= OrderSerializer(order, request.data, partial= True)
    serializer.save()
    
    return Response({'message': f"update order {serializer.data} OK", 'data': serializer.data})

# 刪除訂單
@api_view(['DELETE'])
@try_except
def delete_order(request):
    
    Order.objects.get(id= request.POST.get('id')).delete()
    
    return Response({'message': f"delete order OK"})

# 新增商品
@api_view(['POST'])
@try_except
def add_product(request):
    
    serializer= ProductSerializer(data= request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f" {serializer.data.name} 新增成功 ", 'data': serializer.data}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 取得所有商品資料
@api_view(['GET'])
@try_except
def get_all_product(request):
    all_data= [ProductSerializer(data).data for data in Product.objects.all().iterator()]
    return Response(all_data, status= status.HTTP_200_OK)

# 編輯商品
@api_view(['PUT'])
@try_except
def edit_product(request):
    
    product= Product.objects.get(name= request.POST.get('name'))
    
    serializer= ProductSerializer(product, request.data, partial= True)
    
    serializer.save()
    
    return Response({'message': f"edit OK", 'data': serializer.data}, status= status.HTTP_200_OK)

# 商除商品
@api_view(['DELETE'])
@try_except
def delete_product(request):
    
    Product.objects.get(name= request.POST.get('name')).delete
    
    return Response({'message': f"delete OK"})