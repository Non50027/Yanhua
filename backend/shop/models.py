import os
from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.conf import settings

def icon_name(instance, file_name):
    file_name = f"{instance.name}_icon.{file_name.split('.')[-1]}"
    file_path = os.path.join(f'product_photo/{instance.name}/', file_name)
    
    # 檢查檔案是否已經存在，如果存在則刪除
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)

    return file_path
# 商品
class Product(models.Model):
    name= models.CharField(max_length= 100)
    date= models.DateField(default= timezone.now, blank=True)
    icon= models.ImageField(upload_to= icon_name, default='product_photo/default_icon.png')
    introduction= models.TextField(max_length= 255, blank=True, null=True)
    description= models.TextField(max_length= 255, blank=True, null=True)
    price= models.IntegerField()
    count= models.IntegerField(default= 0)

    def __str__(self):
        return f'{self.name} - {self.price}'

# 用在儲存照片時的路徑與命名
def photo_name(instance, file_name):
    file_name = f"{instance.product.name}_{uuid4().replace('-','')[:3]}.{file_name.split('.')[-1]}"
    return os.path.join(f'product_photo/{instance.product.name}/', file_name)

# 商品照片
class ProductPhoto(models.Model):
    product= models.ForeignKey(Product, related_name= 'photos', on_delete= models.CASCADE)
    photo= models.ImageField(upload_to= photo_name, blank= True, null= True)
    description= models.TextField(max_length= 255, blank= True, null= True)
