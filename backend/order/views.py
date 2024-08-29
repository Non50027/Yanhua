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
    
    # products = {name: Product.objects.get(name=name) for name in request.data['items_name'].split(',')}
    products = [{'name': Product.objects.get(name=name), 'count': int(count)} for name, count in zip(request.data['items_name'].split(','), request.data['items_count'].split(','))]

    data={
        'member': Member.objects.get(name= request.data['member']).pk,
        'addressee': request.data['addressee'],
        'tel': request.data['tel'],
        'address': request.data['address'],
        'total_amount': request.data['total_amount'],
        'items': [{
            # 'product': {
            #     'name': _['name'].name,
            #     'price': _['name'].price,
            # },
            'product': _['name'].pk,
            'count': _['count'],
            'price': _['name'].price * _['count']
        } for _ in products]
    }
    
    serializer= CreateOrder(data= data, partial= True)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        print(Order.objects.get(id= serializer.data['id']))
        return Response({"message": str(Order.objects.get(id= serializer.data['id'])), 'data': serializer.data}, status= status.HTTP_201_CREATED)
    
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
@api_view(['POST'])
@try_except
def email(request, name):
    # 取得會員資料
    member= Member.objects.get(name= name)
    order= Order.objects.get(name= name)
    
    title= '成為合格認證的小羊'
    message= render_to_string('email.html', {
        'user': member,
        'order': order,
    })
    send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [member.email],
        fail_silently= False,
    )
    return Response({'message': '驗證信已送出...請驗證以使用更多功能'}, status= status.HTTP_200_OK)
