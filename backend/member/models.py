import os
from django.db import models

def icon_name(instance, file_name):
        file_name = f"{instance.name}.{file_name.split('.')[-1]}"
        return os.path.join('static/member/', file_name)
    
# 會員
class User(models.Model):
    # 訂單狀態選擇
    class Role(models.TextChoices):
        OWNER= 'owner', '烟花'
        ADMIN= 'ADMIN', '小幫手'
        MEMBER= 'member', '小羊'
    
    
    name= models.CharField(max_length= 50, unique= True)
    display_name= models.CharField(max_length= 50, null= True, blank= True)
    icon= models.ImageField(upload_to= icon_name, blank= True, null= True)
    email= models.EmailField(unique= True)
    password= models.CharField(max_length= 255)
    created_at= models.DateTimeField(auto_now_add= True)
    address= models.TextField(max_length= 255, null= True, blank= True)
    tel= models.CharField(max_length= 12, null= True, blank= True)
    role= models.CharField(max_length= 10, choices= Role.choices, default= Role.MEMBER) 
    
    def __str__(self) -> str:
        return self.display_name if self.display_name else self.name