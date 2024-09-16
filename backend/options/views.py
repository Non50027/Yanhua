import json, os
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from decorators import try_except
from django.conf import settings


@api_view(['POST'])
@try_except
def save_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'options.json')
    with open(file_path, 'w', encoding= 'utf-8') as file:
        json.dump(request.data, file, ensure_ascii= False, indent= 4)
    return Response({'message': '資料儲存成功', 'data': request.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@try_except
def get_data(request):
    file_path = os.path.join(settings.BASE_DIR, 'options.json')
    with open(file_path, 'r', encoding= 'utf-8') as file:
        data= json.load(file)
    return Response(data, status=status.HTTP_200_OK)
