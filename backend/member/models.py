import os, re
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

def icon_name(instance, file_name):
        file_name= f"{instance.name}.{file_name.split('.')[-1]}"
        file_path = os.path.join('member/', file_name)

        # 檢查檔案是否已經存在，如果存在則刪除
        full_path = os.path.join(settings.MEDIA_ROOT, file_path)
        if os.path.exists(full_path):
            os.remove(full_path)

        return file_path
    
# 會員
class Member(models.Model):
    # 訂單狀態選擇
    class Role(models.TextChoices):
        OWNER= '烟花'
        ADMIN= '小幫手'
        MEMBER= '小羊'
    
    name= models.CharField(max_length= 50, unique= True, error_messages= {'unique': '已有重複帳號...禁止冒名頂替'})
    display_name= models.CharField(max_length= 50, null= True, blank= True, default='')
    icon= models.ImageField(upload_to= icon_name, blank= True, null= True)
    email= models.EmailField(unique= True, error_messages= {'unique': "有人用摟"})
    verification= models.BooleanField(default= False, blank= True)
    password= models.CharField(max_length= 255)
    created_at= models.DateTimeField(auto_now_add= True)
    address= models.TextField(max_length= 255, null= True, blank= True, default='')
    tel= models.CharField(max_length= 12, null= True, blank= True, default='')
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