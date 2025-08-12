from rest_framework import serializers
from .models import Result

import cloudinary.uploader


class ResultSerializer(serializers.ModelSerializer):
    
    file = serializers.FileField(write_only = True, required = True)
    
    class Meta:
        model = Result
        fields = ['marks','percentage','declared_on','file_url','file']
        
        extra_kwargs = {
            'file_url':{'read_only':True},
        }
    
    def create(self, validated_data):
        
        file = validated_data.pop("file",None)

        if file:
            uploaded = cloudinary.uploader.upload(file, resource_type = 'auto')

            validated_data['file_url'] = uploaded['secure_url']

        return Result.objects.create(**validated_data)