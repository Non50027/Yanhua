from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 註冊
def register():
    pass

# 修改會員資料
def edit_data():
    pass

# 登入
def login():
    pass

# 登出
def logout():
    pass

# 取得所有會員資料
def get_data():
    pass

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})