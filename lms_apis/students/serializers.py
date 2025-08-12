from rest_framework import serializers

from .models import Student

import cloudinary.uploader

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  
    image = serializers.ImageField(write_only = True, required = False)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    
    class Meta:
        model = Student
        fields = ['id','name', 'phone', 'email', 'pic_url', 'program', 'department', 'image']

        extra_kwargs = {
            'pic_url': {'read_only': True},  # <-- Fix here!
        }
        
    def create(self, validated_data):
        image = validated_data.pop("image", None)
        
        if image:
            uploaded = cloudinary.uploader.upload(image)
            validated_data['pic_url'] = uploaded['secure_url']
        
        
        return Student.objects.create(**validated_data)