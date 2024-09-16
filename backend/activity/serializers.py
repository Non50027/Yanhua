from rest_framework import serializers
from member.models import Member
from .models import Activity, ActivityPhoto

class Member(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['name', 'display_name', 'email', 'created_at', 'role']

class CreateActivityPhoto(serializers.ModelSerializer):
    author= Member()
    
    class Meta:
        model= ActivityPhoto
        fields= ['photo', 'author', 'description']

class CreateActivity(serializers.ModelSerializer):
    class Meta:
        model= Activity
        fields= ['title', 'address', 'start_date', 'stop_date', 'description', 'image', 'url', 'photo']

class GetActivityPhoto(serializers.ModelSerializer):
    author= Member()
    class Meta:
        model= ActivityPhoto
        fields= ['photo', 'author', 'description']
        
class GetActivity(serializers.ModelSerializer):
    photo= GetActivityPhoto
    class Meta:
        model= Activity
        fields= ['title', 'address', 'start_date', 'stop_date', 'description', 'image', 'url', 'photo']