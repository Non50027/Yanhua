import os
from uuid import uuid4
from django.utils import timezone
from django.db import models
from login.models import User

# 訂單
class Order(models.Model):
    
    # 訂單狀態選擇
    class OrderStatus(models.TextChoices):
        PENDING= 'pending', '等待確認'
        PROCESSED= 'processed', '等待出貨'
        SHIPPED= 'shipped', '已出貨'
        DELIVERED= 'delivered', '已交付'
        CANCELED= 'canceled', '取消'
    
    id= models.CharField(max_length= 10, unique=True, blank=True, primary_key= True)
    user= models.ForeignKey(User, related_name= 'order', on_delete= models.CASCADE)  # 連結會員資料
    address= models.TextField(max_length= 255)  # 寄送地址
    tel= models.CharField(max_length= 12)   # 連絡電話
    status= models.CharField(max_length= 15, choices= OrderStatus.choices, default= OrderStatus.PENDING)    # 訂單狀態
    created_at= models.DateTimeField(auto_now_add= True)    # 創建日期
    total_amount= models.DecimalField(max_digits= 10, decimal_places= 2)  
    
    # 複寫 save 建立一個隨機碼作為 ID
    def save(self, *args, **kwargs):
        self.id= timezone.now().strftime('%Y%m%d%H%M%S')+ str(uuid4().replace('-','')[:6])
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'#{self.id}: {self.user} 狀態: {self.status} 金額: {self.total_amount}'

# 商品
class Product(models.Model):
    name= models.CharField(max_length= 100)
    Introduction= models.TextField(max_length= 255, blank=True, null=True)
    description= models.TextField(max_length= 255, blank=True, null=True)
    price= models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return f'{self.name} - {self.price}'

# 用在儲存照片時的路徑與命名
def photo_name(instance, file_name):
    file_name = f"{instance.product.name}{uuid4().replace('-','')[:3]}.{file_name.split('.')[-1]}"
    return os.path.join(f'static/product_photo/{instance.product.name}/', file_name)

# 商品照片
class ProductPhoto(models.Model):
    product= models.ForeignKey(Product, related_name= 'photos', on_delete= models.CASCADE)
    photo= models.ImageField(upload_to= photo_name, blank= True, null= True)
    description= models.TextField(max_length= 255, blank= True, null= True)
    
# 訂單內商品
class OrderItem(models.Model):
    order= models.ForeignKey(Order, related_name= 'items', on_delete= models.CASCADE)
    product= models.ForeignKey(Product, related_name= 'items', on_delete= models.CASCADE)
    count= models.PositiveIntegerField()
    price= models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return f"#{self.order.id} 名稱: {self.product.name} 數量: {self.count} 價格: {self.get_total_price()} "

    def get_total_price(self):
        return self.count * self.price