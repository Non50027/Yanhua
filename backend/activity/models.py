import os
from uuid import uuid4
from django.db import models
from member.models import Member

# 用在儲存照片時的路徑與命名
def title_photo(instance, file_name):
    file_name = f"{instance.title}{file_name.split('.')[-1]}"
    return os.path.join(f'static/activity/{instance.title}/', file_name)

class Activity(models.Model):
    
    title = models.CharField(max_length=100)
    address= models.TextField(max_length= 255, blank= True, null=True)
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField()
    description= models.TextField(max_length= 255, blank= True, null= True)
    image= models.ImageField(upload_to= title_photo)
    url= models.URLField()
    
    def __str__(self) -> str:
        return self.title

def photo_name(instance, file_name):
    file_name = f"{instance.activity.title}_{uuid4().replace('-','')[:3]}.{file_name.split('.')[-1]}"
    return os.path.join(f'static/activity/{instance.activity.title}/', file_name)


class ActivityPhoto(models.Model):
    
    activity= models.ForeignKey(Activity, related_name= 'photo', on_delete= models.CASCADE)
    photo= models.ImageField(upload_to= photo_name)
    author= models.ForeignKey(Member, on_delete= models.CASCADE, blank= True, null= True)
    description= models.TextField(max_length= 255, blank= True, null= True)