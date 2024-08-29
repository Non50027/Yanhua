from uuid import uuid4
from django.utils import timezone
from django.db import models
from member.models import Member
from shop.models import Product

# 訂單
class Order(models.Model):
    
    # 訂單狀態選擇
    class OrderStatus(models.TextChoices):
        PENDING= 'pending', '等待確認'
        PROCESSED= 'processed', '等待出貨'
        SHIPPED= 'shipped', '已出貨'
        DELIVERED= 'delivered', '已交付'
        CANCELED= 'canceled', '取消'
    
    id= models.CharField(max_length= 20, unique=True, blank=True, primary_key= True)
    status= models.CharField(max_length= 15, choices= OrderStatus.choices, default= OrderStatus.PENDING)    # 訂單狀態
    member= models.ForeignKey(Member, related_name= 'order', on_delete= models.CASCADE)  # 連結會員資料
    addressee= models.TextField(max_length= 6)
    address= models.TextField(max_length= 255)  # 寄送地址
    tel= models.CharField(max_length= 12)   # 連絡電話
    created_at= models.DateTimeField(auto_now_add= True)    # 創建日期
    total_amount= models.IntegerField()
    
    # 複寫 save 建立一個隨機碼作為 ID
    def save(self, *args, **kwargs):
        self.id= timezone.now().strftime('%Y%m%d')+ str(uuid4()).replace('-','')[:7]
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'#{self.id}: {self.member} 狀態: {self.status} 金額: {self.total_amount}'

# 訂單內商品
class Item(models.Model):
    order= models.ForeignKey(Order, related_name= 'items', on_delete= models.CASCADE)
    product= models.ForeignKey(Product, related_name= 'items', on_delete= models.CASCADE)
    count= models.PositiveIntegerField()
    price= models.IntegerField()

    def __str__(self):
        return f"#{self.order.id} 名稱: {self.product.name} 數量: {self.count} 價格: {self.get_total_price()} "

    def get_total_price(self):
        return self.count * self.price