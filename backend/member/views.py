from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from .models import Member
from .serializers import MemberSerializer, CreateMemberSerializer
from decorators import try_except
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# 註冊 
@api_view(['POST'])
@try_except
def save_member(request):
    
    serializer= CreateMemberSerializer(data= request.data)
    
    # print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": f"{serializer.data['display_name'] if serializer.data['display_name'] else serializer.data['name']}", "data": serializer.data}, status= status.HTTP_201_CREATED)
    
    else:
        raise ValidationError(serializer.errors)

# 發送驗證信
@api_view(['POST'])
@try_except
def verification_email(request):
    print(request.data['email'])
    # 取得會員資料
    member= Member.objects.get(name= request.data['name'])
    
    token= VerificationEmail()
    # 生成一個專屬身分令牌
    token= token.make_token(member)
    # 加密會員 ID
    uid= urlsafe_base64_encode(force_bytes(member.pk))
    # 生成驗證連結
    verification_link= f'http://localhost:5173/member/{member.name}/{uid}/{token}/'
    
    title= '成為合格認證的小羊'
    message= render_to_string('email.html', {
        'user': member,
        'verification_link': verification_link,
    })
    send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [request.data['email']],
        fail_silently= False,
    )
    return Response({'message': '驗證信已送出...請驗證以使用更多功能'}, status= status.HTTP_200_OK)

# 驗證透過連結點進來的會員
@api_view(['GET'])
@try_except
def activate_account(request, uidb64, token):
    
    uid= force_str(urlsafe_base64_decode(uidb64))
    member= Member.objects.get(pk= uid)
    ck= VerificationEmail()
    if ck.check_token(member, token):
        member.verification= True
        member.save()
        
        return Response({"message": "信箱驗證成功！", 'data': MemberSerializer(member).data}, status= status.HTTP_200_OK)
    else:
        return Response({"error": "信箱驗證失敗"}, status= status.HTTP_400_BAD_REQUEST)

# 修改會員資料 
@api_view(['PUT'])
@try_except
def edit_data(request):
    
    member= Member.objects.get(name= request.data['name'])
    
    serializer= MemberSerializer(member, data= request.data, partial= True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "更改成功", 'data': serializer.data}, status= status.HTTP_200_OK)
    
    else:
        raise ValidationError(serializer.errors)
    
# 登入 login/
@api_view(['POST'])
@try_except
def login(request):
    member= Member.objects.get(name= request.data['name'])
    if request.data['password']== member.password:
        return Response({'message': str(member)}, status= status.HTTP_200_OK)
    else:
        return Response({'error': '密碼不正確'}, status= status.HTTP_400_BAD_REQUEST)

# 登出 logout/
def logout():
    pass

# 取得所有會員資料 
@api_view(['GET'])
@try_except
def get_all_data(request):
    all_data= [MemberSerializer(member).data for member in Member.objects.all().iterator()]
    return Response(all_data)

# 取得會員資料 
@api_view(['GET'])
@try_except
def get_data(request):
    member= Member.objects.get(name= request.GET.get('name'))
    return Response(MemberSerializer(member).data)

class VerificationEmail(PasswordResetTokenGenerator):
    def _make_hash_value(self, member, timestamp):
        # 根據其他屬性來生成哈希值，不依賴 last_login
        return f"{member.pk}{timestamp}{member.name}"
