from rest_framework import serializers
from .models import Assignment

import cloudinary.uploader


class AssignmentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only = True, required = True)
    
    class Meta:
        model = Assignment
        
        fields = ['announcement', 'published_on','deadline', 'file','file_url']

        extra_kwargs = {
            'file_url':{'read_only': True }
        }
        
    def create(self, validated_data):
        file = validated_data.pop("file",None)
        
        if file:
            uploaded = cloudinary.uploader.upload(file, resource_type = 'auto')

            validated_data['file_url'] = uploaded['secure_url']
            
        return Assignment.objects.create(**validated_data)