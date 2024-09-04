from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import GetProduct, CreateProduct
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from decorators import try_except
from .models import Product

# 新增商品
@api_view(['POST'])
@try_except
def add(request):
    serializer= CreateProduct(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f" {serializer.data['name']} 新增成功 ", 'data': serializer.data}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 取得所有商品資料
@api_view(['GET'])
@try_except
def get(request):
    all_data= [GetProduct(data).data for data in Product.objects.all().iterator()]
    return Response(all_data, status= status.HTTP_200_OK)

# 編輯商品
@api_view(['PUT'])
@try_except
def edit(request):
    
    product= Product.objects.get(name= request.POST.get('name'))
    
    serializer= GetProduct(product, request.data, partial= True)
    
    serializer.save()
    
    return Response({'message': f"edit OK", 'data': serializer.data}, status= status.HTTP_200_OK)

# 刪除商品
@api_view(['DELETE'])
@try_except
def delete(request):
    
    Product.objects.get(name= request.POST.get('name')).delete
    
    return Response({'message': f"delete OK"})