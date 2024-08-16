from rest_framework import serializers
from member.models import Member
from .models import Activity, ActivityPhoto

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['name', 'display_name', 'email', 'verification', 'address', 'tel', 'created_at', 'role']

class ActivityPhotoSerializer(serializers.ModelSerializer):
    
    author= MemberSerializer()
    
    class Meta:
        model= ActivityPhoto
        fields= ['photo', 'author', 'description']

class ActivitySerializer(serializers.ModelSerializer):
    
    photo= ActivityPhotoSerializer(many= True)
    
    class Meta:
        model= Activity
        fields= ['title', 'address', 'start_date', 'stop_date', 'description', 'image', 'url', 'photo']

