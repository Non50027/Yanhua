import os
from django.db import models
from django.core.exceptions import ValidationError
import re

def icon_name(instance, file_name):
        file_name= f"{instance.name}.{file_name.split('.')[-1]}"
        return os.path.join('static/member/', file_name)
    
# 會員
class Member(models.Model):
    # 訂單狀態選擇
    class Role(models.TextChoices):
        OWNER= 'owner', '烟花'
        ADMIN= 'ADMIN', '小幫手'
        MEMBER= 'member', '小羊'
    
    name= models.CharField(max_length= 50, unique= True, error_messages= {'unique': '已有重複帳號...禁止冒名頂替'})
    display_name= models.CharField(max_length= 50, null= True, blank= True)
    icon= models.ImageField(upload_to= icon_name, blank= True, null= True)
    email= models.EmailField(unique= True, error_messages= {'unique': "有人用摟"})
    verification= models.BooleanField(default= False, blank= True)
    password= models.CharField(max_length= 255)
    created_at= models.DateTimeField(auto_now_add= True)
    address= models.TextField(max_length= 255, null= True, blank= True)
    tel= models.CharField(max_length= 12, null= True, blank= True)
    role= models.CharField(max_length= 10, choices= Role.choices, default= Role.MEMBER, blank= True) 
    
    
    def clean(self):
        # 只允許英文字母和 _
        if not re.match(r'^[A-Za-z0-9_]*$', self.name):
            raise ValidationError('帳號只能使用英文、數字、_')
            
    def save(self, *args, **kwargs):
        self.clean()  # 保存前進行驗證
        super(Member, self).save(*args, **kwargs)
        
        
    def __str__(self) -> str:
        return self.display_name if self.display_name else self.name