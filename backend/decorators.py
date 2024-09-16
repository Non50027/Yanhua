from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from smtplib import SMTPException, SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError, SMTPAuthenticationError
from member.models import Member
from django.core.exceptions import ObjectDoesNotExist, DisallowedHost  

def try_except(functionName):
    
        @wraps(functionName)
        def inner(*args, **kwargs):
            
            try:
                return functionName(*args, **kwargs)
            
            # 不允許的請求
            except DisallowedHost as e:
                host = args[0].get_host()  # 從請求中獲取主機名
                print(f"不允許的請求 - {host} ")
                return Response(
                    {'error': f"The host '{host}' is not allowed. You may have connected to the wrong server or domain."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # 處理會員資料
            except Member.DoesNotExist as e:
                print('未發現小羊')
                return Response({'error': {'name':['未發現小羊']}}, status= status.HTTP_404_NOT_FOUND)
            
            # 處理其他資料
            except ObjectDoesNotExist as e:
                print('沒有資料')
                return Response({'error': '沒有資料'}, status= status.HTTP_404_NOT_FOUND)
            
            # 捕捉序列化過程中的 ValidationError
            except ValidationError as e:
                print(str(e))
                print(e.detail)
                print('序列化錯誤')
                return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
            
            # 處理身份驗證錯誤
            except SMTPAuthenticationError as e:
                print('身份驗證失敗')
                return Response({'error': "身份驗證失敗"}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
            # 處理收件人地址被拒絕的情況
            except SMTPRecipientsRefused as e:
                print('收件人地址無效或被拒絕')
                return Response({'error': "收件人地址無效或被拒絕"}, status= status.HTTP_400_BAD_REQUEST)
            # 處理發件人地址被拒絕的情況
            except SMTPSenderRefused as e:
                print('發件人地址被拒絕')
                return Response({'error': "發件人地址被拒絕"}, status= status.HTTP_400_BAD_REQUEST)
            # 處理數據錯誤
            except SMTPDataError as e:
                print('伺服器無法處理郵件數據')
                return Response({'error': "伺服器無法處理郵件數據"}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
            # 處理其他 SMTP 異常
            except SMTPException as e:
                print('發送郵件時發生錯誤')
                return Response({'error': f"發送郵件時發生錯誤: {str(e)}"}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # 資料庫錯誤
            except IntegrityError as e:
                error_message = str(e)
                if "Duplicate entry" in error_message:
                    # 處理唯一性約束違反
                    print("數據重複")
                    return Response({'error': '數據重複'}, status=status.HTTP_400_BAD_REQUEST)
                elif "FOREIGN KEY constraint" in error_message:
                    # 處理外鍵約束違反
                    print("缺少外鍵依附值")
                    return Response({'error': '缺少外鍵依附值'}, status=status.HTTP_400_BAD_REQUEST)
                elif "NOT NULL constraint" in error_message:
                    # 處理非空約束違反
                    print("缺少必要值")
                    return Response({'error': '缺少必要值'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # 處理其他錯誤
                    print(error_message, "未知資料庫約束錯誤")
                    return Response({'error': '未知資料庫約束錯誤'}, status=status.HTTP_400_BAD_REQUEST)
            
            # 處理其他所有未捕捉到的異常
            except Exception as e:
                print(str(e), '其他錯誤')
                return Response({'error': str(e)}, status= status.HTTP_400_BAD_REQUEST)
            
        return inner