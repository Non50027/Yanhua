from django.shortcuts import render
from .serializers import ActivitySerializer, ActivityPhotoSerializer
from rest_framework.decorators import api_view
from decorators import try_except
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .models import Activity

# 新活動 
@api_view(['POST'])
@try_except
def add_activity(request):
    
    serializer= ActivitySerializer(data= request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f"{serializer.data} 創建成功"}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 為活動增加照片
@api_view(['POST'])
@try_except
def add_photo(request):
    
    serializer= ActivityPhotoSerializer(data= request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f"add photo OK"}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 取得所有活動
@api_view(['GET'])
@try_except
def get_activities(request):
    
    all_data= [ActivitySerializer(data) for data in Activity.objects.all().iterator()]
    return Response(all_data)

# 更新活動
@api_view(['PUT'])
@try_except
def update_activity(request):
    
    activity= Activity.objects.get(title= request.POST.get('title'))

    serializer= ActivitySerializer(activity, data= request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f"{serializer.data} 更改成功"}, status= status.HTTP_200_OK)
    
    else:
        raise ValidationError(serializer.errors)

# 刪除活動 
@api_view(['DELETE'])
@try_except
def delete_activity(request):
    
    Activity.objects.get(title= request.POST.get('title')).delete()
    return Response({'message': '刪除成功'})
