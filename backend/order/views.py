from django.shortcuts import render
from rest_framework.decorators import api_view
from shop.models import Product
from member.models import Member
from .serializers import CreateOrder, GetOrder
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from decorators import try_except
from django.template.loader import render_to_string
from .models import Order

# 建立訂單
@api_view(['POST'])
@try_except
def add(request):
    
    serializer= CreateOrder(data= request.data)
    
    if serializer.is_valid():
        order= serializer.save()
        email(order)
        return Response({"message": str(order), 'data': serializer.data}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 取得一筆訂單
@api_view(['GET'])
@try_except
def get(request):
    
    order= Order.objects.get(id= request.GET.get('id'))
    
    serializer= GetOrder(order)
    
    return Response(serializer.data)
    
# 更新訂單
@api_view(['PUT'])
@try_except
def edit(request):
    
    order= Order.objects.get(id= request.POST.get('id'))
    
    serializer= CreateOrder(order, request.data, partial= True)
    serializer.save()
    
    return Response({'message': f"update order {serializer.data} OK", 'data': serializer.data})

# 刪除訂單
@api_view(['DELETE'])
@try_except
def delete(request):
    
    Order.objects.get(id= request.POST.get('id')).delete()
    
    return Response({'message': f"delete order OK"})

# 發送確認信
@try_except
def email(order):
    
    order_detail= GetOrder(order).data
    
    message= render_to_string(
            template_name= 'orderEmail.html', 
            context= {
            'data': order_detail,
        })
    send_mail(
        '穴穴尼把羊帶回家',
        '',
        settings.EMAIL_HOST_USER,
        [order_detail['member']['email']],
        fail_silently= False,
        html_message= message
    )
